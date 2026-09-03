# Optional artifact schemas

These versioned JSON Schemas support validation and tool integration when a project chooses the repository's machine-readable artifact structure. They do not replace the teaching decisions in `SKILL.md`, require an existing project to change its equivalent structure, or grant permission for paid services, account access, uploads, rendering, or publication.

| Schema | Live fixtures | Status |
| --- | --- | --- |
| [Learning brief v1](./brief.schema.json) | Both public `examples/*/brief.json` files | Validated in CI |
| [Visual plan v1](./visual-plan.schema.json) | Both public `examples/*/visual-plan.json` files and their dialogue line IDs | Validated in CI |

Run the repository validator after changing a schema or fixture:

```bash
python -m pip install --requirement requirements-dev.txt
python scripts/validate_repository.py
```

Keep version 1 backward compatible. If a required field changes meaning, a field is removed, or the accepted data shape becomes incompatible, add a new schema version instead of silently redefining existing artifacts. Subject-specific fields belong in a future version only after repeated use shows that they are part of the shared teaching contract.
