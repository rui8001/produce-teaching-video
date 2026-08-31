# Real-user trial results

This ledger records only real, voluntary trial activity. It starts at zero and must never contain invented invitations, users, feedback, testimonials, or success claims.

## Current aggregate

**Last updated:** 2026-08-31

| Measure | Count |
| --- | ---: |
| Invitations sent | 0 |
| Volunteers accepted | 0 |
| Route A attempts | 0 |
| Route B attempts | 0 |
| Completed without help | 0 |
| Public trial Issues | 0 |
| Confirmed blockers | 0 |

No real-user feedback has been collected yet. Maintainer self-tests and automated checks are documented elsewhere and do not count here.

## Anonymous trial ledger

Add one row only after a real invitation is sent. Use an anonymous ID; never add a person's name, email address, employer, social account, private topic, or private response.

| Test ID | Invitation date | Voluntary acceptance | Route | Outcome | First confirmed problem | Public Issue | Anonymous summary allowed | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | No trials recorded | — | — | — | Awaiting volunteers |

Allowed outcome values are defined in the [testing guide](./USER_TESTING.md). If a tester does not allow an anonymous summary, record only the aggregate count and operational status needed for the release gate.

## Confirmed-problem triage

| Reference | Severity | Reproduction status | Resolution or tracking link | v0.2.0 gate |
| --- | --- | --- | --- | --- |
| — | — | No confirmed trial problems | — | Still closed |

## Update rules

1. Recalculate the aggregate from real records; do not estimate or round upward.
2. Include failed and stopped trials instead of reporting only successful attempts.
3. Link a public Issue only with permission. A GitHub username is public identity.
4. Paraphrase private feedback only when anonymous-summary permission is checked; do not quote private messages.
5. Keep the v0.2.0 gate closed until at least three real people have been invited and confirmed problems are fixed or transparently tracked.
6. Commit each material update so the public history shows when evidence was recorded.
