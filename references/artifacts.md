# Artifact contract

Use an equivalent structure when the host project already has one.

```text
work/<date>-<slug>/
  00-brief.json
  01-script.txt
  01-dialogue.json
  02-audio/
    narration.wav
    alignment.json
    captions.srt
  03-sources/
    source-ledger.md
  04-plan/
    visual-plan.json
  05-assets/
  06-composition/
  07-review/
  08-production-status.md
  09-final-qc.md
  final/
```

- `00-brief.json`: learner, objective, prerequisite, misconception, model limits, transfer task, output, style, authorization.
- `01-script.txt`: only words actually spoken.
- `01-dialogue.json`: speakers, lines, emphasis, pauses, performance, and teaching function.
- `source-ledger.md`: claim, source, evidence class, allowed inference, unresolved issue, redistribution boundary.
- `visual-plan.json`: semantic shot, active role, viewer takeaway, initial/final state, meaningful changes, evidence, label and transition.
- `08-production-status.md`: current checkpoint, locks, checks, authorization, issue, next action, rollback.
- `09-final-qc.md`: subject, learning, audiovisual, source, copyright, privacy and output evidence.

Use portable relative paths internally. Store a separate absolute path only when an external editor handoff requires it.

When machine-readable compatibility is useful, validate `00-brief.json` and `visual-plan.json` against the optional [learning brief](../schemas/brief.schema.json) and [visual plan](../schemas/visual-plan.schema.json) v1 schemas. The schemas check the shared artifact contract; they do not replace an equivalent host-project structure or grant authorization for later production steps.
