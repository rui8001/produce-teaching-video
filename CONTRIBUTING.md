# Contributing

Issues and pull requests are welcome when they improve the reusable teaching method without importing private project content.

Before submitting:

1. Keep the Skill independent of one subject, brand, presenter, or video framework.
2. Use redistributable examples and remove personal, student, account, and production data.
3. Keep detailed conditional guidance in `references/` and link it from `SKILL.md`.
4. Run the official Skill validator and inspect all changed Markdown and YAML.
5. Explain the learner or production failure that the change fixes.

Changes to required artifacts or gates should include migration notes in `CHANGELOG.md`.

## Local quality check

The repository uses one deterministic validator locally and in GitHub Actions:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate_repository.py
```

It validates the Skill frontmatter, UI metadata, JSON examples, local Markdown links, SVG syntax, and common credential or personal-path patterns. A passing scan reduces accidental exposure risk but does not replace a human privacy and licensing review.
