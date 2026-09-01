# Codex for Open Source application readiness

This document tracks repository evidence only. Personal application fields must remain outside the public repository.

## Repository evidence

| Signal | Evidence to collect | Current state |
| --- | --- | --- |
| Public open source | Public repository and MIT license | Ready |
| Maintainer role | Repository ownership and ongoing maintenance | Ready; continue building history |
| Clear ecosystem value | A reusable method for teaching-video production across subjects | [Physics example](../examples/solar-eclipse/README.md) and [Git procedure example](../examples/git-merge-conflict/README.md) complete |
| Meaningful usage | Real testers, public Issues when appropriate, and consented case summaries | [Trial kit and zero-based ledger](./USER_TEST_RESULTS.md) ready; 0 invitations and 0 responses recorded |
| Active maintenance | Issue triage, meaningful commits, releases, and transparent changelog | Active; dated [evidence log](#evidence-log) and changelog maintained |
| Reproducibility | Fresh-install test and complete examples | [Fresh install passed](./FRESH_INSTALL_TEST.md); both [physics](../examples/solar-eclipse/README.md) and [procedural](../examples/git-merge-conflict/README.md) walkthroughs complete |
| Responsible automation | Automated quality, privacy, and release checks | [Passing workflow](https://github.com/rui8001/produce-teaching-video/actions/runs/32956656619) |
| API-credit plan | PR review, issue triage, regression evaluation, and release automation | Draft direction ready |

## Private fields the maintainer must prepare

Do not commit any of these values:

- Legal first and last name.
- Email address associated with the ChatGPT account.
- Public GitHub username and a publicly visible GitHub profile.
- OpenAI Organization ID from the API platform account.
- A truthful statement that the applicant is the primary maintainer.
- Up-to-date repository usage signals available at application time.
- Final approval of each application answer before submission.

The application form currently limits the repository qualification, API-credit use, and optional additional-information answers to 500 characters each. Drafts can be maintained privately until the evidence is current.

## Evidence log

Add only verifiable public links or anonymous aggregate counts.

| Date | Evidence | Public link or aggregate | Notes |
| --- | --- | --- | --- |
| 2026-08-25 | Initial open-source release | [`v0.1.0`](https://github.com/rui8001/produce-teaching-video/releases/tag/v0.1.0) | Standalone Skill published |
| 2026-08-25 | Public maintenance backlog | [Open Issues](https://github.com/rui8001/produce-teaching-video/issues) | Five outcome-based maintenance tasks opened |
| 2026-08-26 | Automated public-package validation | [Repository quality run](https://github.com/rui8001/produce-teaching-video/actions/runs/32956656619) | Skill, metadata, examples, links, SVG, and sensitive-data checks passed |
| 2026-08-27 | Isolated fresh-install and Codex discovery test | [Verification record](./FRESH_INSTALL_TEST.md) | Public download, validation, metadata, and discovery passed without credentials or paid services |
| 2026-08-28 | Source-checked physics walkthrough | [Solar-eclipse example](../examples/solar-eclipse/README.md) | Brief, source ledger, script, visual plan, self-authored SVG, status, and QC boundaries published |
| 2026-08-29 | Verified v0.1.1 tag | [Release verification](./RELEASE_VERIFICATION_V0.1.1.md) | Release commit passed CI and a fresh tagged checkout passed validation and Codex discovery; GitHub Release page pending maintainer confirmation |
| 2026-08-30 | Reproducible non-physics walkthrough | [Git merge-conflict example](../examples/git-merge-conflict/README.md) | Official sources, deterministic temporary-repository evidence, script, visual plan, self-authored SVG, status, and QC boundaries published |
| 2026-08-31 | Consent-safe real-user trial kit | [Testing guide](./USER_TESTING.md) and [results ledger](./USER_TEST_RESULTS.md) | Invitation, no-coaching run sheet, anonymous feedback form, and public Issue template are ready; no invitations or feedback counted yet |
| 2026-09-01 | Versioned learning-brief contract | [JSON Schema](../schemas/brief.schema.json) | Both subject-diverse public briefs are validated against the optional Draft 2020-12 schema in CI |

## Application gate

The application is ready for final review when:

- Both v0.1.1 and v0.2.0 represent meaningful completed work.
- The physics and non-physics examples are reproducible.
- Automated checks are passing.
- Real-user feedback has been recorded truthfully.
- Usage metrics and all three short answers have been refreshed immediately before submission.
- The maintainer has personally checked the private identity fields and authorized submission.
