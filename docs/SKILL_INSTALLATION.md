# Skill Installation

The bundled skill lives at:

```text
skills/neetcode-prep-coach/
```

Install it into Codex by copying that folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R <PACKAGE_ROOT>/skills/neetcode-prep-coach ~/.codex/skills/
```

Restart Codex after installation so the skill registry refreshes.

Use it with an explicit package root:

```text
Use $neetcode-prep-coach with package root <PACKAGE_ROOT>.
```

The package root is intentionally not baked into the skill. If you move this package, initialize the skill with the new path.
