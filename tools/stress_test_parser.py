from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any

from tools.fetch_and_generate import (
    LEETCODE_GRAPHQL_URL,
    QUESTION_QUERY,
    extract_official_examples,
    html_to_lines,
    request_graphql,
    similar_questions_from_detail,
    split_problem_content,
)


ROOT = Path(__file__).resolve().parents[1]

PROBLEMSET_QUERY = """
query problemsetQuestionList($categorySlug: String, $limit: Int, $skip: Int, $filters: QuestionListFilterInput) {
  problemsetQuestionList: questionList(
    categorySlug: $categorySlug
    limit: $limit
    skip: $skip
    filters: $filters
  ) {
    total: totalNum
    questions: data {
      questionFrontendId
      title
      titleSlug
      difficulty
      paidOnly: isPaidOnly
    }
  }
}
"""


def fetch_problem_list(limit: int) -> list[dict[str, Any]]:
    questions: list[dict[str, Any]] = []
    total: int | None = None
    while len(questions) < limit:
        page_limit = min(100, limit - len(questions))
        data = request_graphql(
            PROBLEMSET_QUERY,
            {
                "categorySlug": "",
                "skip": len(questions),
                "limit": page_limit,
                "filters": {},
            },
            referer="https://leetcode.com/problemset/",
        )
        page = data["problemsetQuestionList"]
        total = page["total"]
        batch = page["questions"]
        if not batch:
            break
        questions.extend(batch)
        if total is not None and len(questions) >= total:
            break
    return questions[:limit]


def raw_similar_count(detail: dict[str, Any]) -> int:
    raw = detail.get("similarQuestions")
    if not raw:
        return 0
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError:
        return 1
    return len(parsed) if isinstance(parsed, list) else 0


def has_constraint_signal(detail: dict[str, Any]) -> bool:
    for line in html_to_lines(detail.get("content")):
        if line.lower().startswith("constraints"):
            return True
        if "you may assume" in line.lower():
            return True
    return False


def audit_detail(summary: dict[str, Any], detail: dict[str, Any]) -> dict[str, Any]:
    sections = split_problem_content(detail.get("content"))
    examples = extract_official_examples(detail.get("content"))
    similar = similar_questions_from_detail(detail)
    issues: list[str] = []

    if not sections["description"]:
        issues.append("missing_description")
    if any(line.lower().startswith("example") for line in sections["description"]):
        issues.append("example_leaked_into_description")
    if has_constraint_signal(detail) and not sections["constraints"]:
        issues.append("missing_constraints")
    if not examples:
        issues.append("missing_examples")
    else:
        if any(not example.get("input") for example in examples):
            issues.append("example_missing_input")
        if any(not example.get("output") for example in examples):
            issues.append("example_missing_output")
    if raw_similar_count(detail) and not similar:
        issues.append("similar_questions_parse_failed")

    return {
        "id": summary.get("questionFrontendId"),
        "title": summary.get("title"),
        "slug": summary.get("titleSlug"),
        "difficulty": summary.get("difficulty"),
        "description_lines": len(sections["description"]),
        "constraint_lines": len(sections["constraints"]),
        "examples": len(examples),
        "examples_with_explanation": sum(1 for example in examples if example.get("explanation")),
        "has_follow_up": bool(sections["follow_up"]),
        "similar_questions": len(similar),
        "issues": issues,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Stress test the LeetCode HTML parser against a broad public problem sample."
    )
    parser.add_argument("--limit", type=int, default=1000, help="Number of problem-list entries to inspect")
    parser.add_argument("--sleep", type=float, default=0.03, help="Delay between detail requests")
    parser.add_argument(
        "--report",
        type=Path,
        default=ROOT / "indexes" / "parser_stress_report.json",
        help="Where to write the JSON audit report",
    )
    args = parser.parse_args()

    summaries = fetch_problem_list(args.limit)
    skipped_paid = [item for item in summaries if item.get("paidOnly")]
    public_summaries = [item for item in summaries if not item.get("paidOnly")]

    results = []
    request_errors = []
    for index, summary in enumerate(public_summaries, start=1):
        slug = summary["titleSlug"]
        try:
            detail = request_graphql(
                QUESTION_QUERY,
                {"titleSlug": slug},
                referer=f"https://leetcode.com/problems/{slug}/",
            )["question"]
            results.append(audit_detail(summary, detail))
        except Exception as exc:
            request_errors.append(
                {
                    "slug": slug,
                    "title": summary.get("title"),
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
        if args.sleep and index < len(public_summaries):
            time.sleep(args.sleep)

    issue_results = [item for item in results if item["issues"]]
    report = {
        "source": LEETCODE_GRAPHQL_URL,
        "requested_limit": args.limit,
        "listed": len(summaries),
        "skipped_paid": len(skipped_paid),
        "audited_public": len(results),
        "request_errors": request_errors,
        "issue_count": len(issue_results),
        "issues": issue_results,
        "summary": {
            "with_follow_up": sum(1 for item in results if item["has_follow_up"]),
            "with_similar_questions": sum(1 for item in results if item["similar_questions"]),
            "with_explanations": sum(1 for item in results if item["examples_with_explanation"]),
            "total_examples": sum(item["examples"] for item in results),
        },
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({key: report[key] for key in ["requested_limit", "listed", "skipped_paid", "audited_public", "issue_count"]}, indent=2))
    if request_errors:
        print(f"Request errors: {len(request_errors)}")
    if issue_results:
        print(f"Parser issues written to {args.report}")
        raise SystemExit(1)
    print(f"Parser stress report written to {args.report}")


if __name__ == "__main__":
    main()
