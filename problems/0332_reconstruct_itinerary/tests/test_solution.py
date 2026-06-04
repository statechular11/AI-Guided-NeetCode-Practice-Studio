from pathlib import Path

from common.runner import run_problem


def test_solution():
    assert run_problem(Path(__file__).resolve().parents[1]) == 0
