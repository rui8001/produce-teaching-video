# Codex for Open Source application worksheet

This maintainer worksheet maps the public repository evidence to the current application fields without storing private identity values. It is a draft, not a submitted application or a claim of eligibility.

**Official sources checked on 2026-09-02:**

- [Codex for Open Source application](https://openai.com/form/codex-for-oss/)
- [Codex for Open Source Program Terms](https://learn.chatgpt.com/docs/codex-for-oss-terms)
- [OpenAI Organization settings](https://platform.openai.com/settings/organization/general)

The official form and terms may change. Reopen them immediately before submission. The current form says applications are reviewed on a rolling basis and asks for accurate maintainer, repository, and planned-use information; submission does not guarantee selection.

## Current decision

**Not ready to submit.** The public maintenance and reproducibility evidence is credible, but meaningful usage is still missing: 0 real-user invitations and 0 responses are recorded. The v0.2.0 release gate therefore remains closed.

## Official field map

| Form field | Repository-safe preparation | Final action |
| --- | --- | --- |
| First name | Do not store in this repository | Maintainer enters personally |
| Last name | Do not store in this repository | Maintainer enters personally |
| ChatGPT account email | Do not store in this repository | Maintainer enters personally |
| GitHub username | Public profile must be visible; do not duplicate personal fields here | Maintainer verifies and enters personally |
| GitHub repository URL | `https://github.com/rui8001/produce-teaching-video` | Refresh visibility before submission |
| Primary or core maintainer | Repository ownership is public evidence, but the role is a personal attestation | Maintainer selects truthfully |
| Why the repository qualifies | Draft below; currently discloses early adoption | Refresh after real-user testing |
| Interest in Codex Security | Optional program choice | Maintainer decides personally |
| Interest in API credits | Public maintenance use plan drafted below | Maintainer decides personally |
| OpenAI Organization ID | Do not store in this repository | Maintainer retrieves and enters personally |
| How API credits will be used | Draft below | Review against the final intended workflows |
| Anything else | Optional draft below | Keep only accurate, non-confidential facts |
| Program Terms and submission | Cannot be pre-approved by repository automation | Maintainer reads, agrees, and explicitly authorizes submission |

## Evidence snapshot

Snapshot date: **2026-09-02**. Refresh every count immediately before applying.

| Signal | Current public evidence |
| --- | --- |
| Public open source | Public MIT-licensed repository |
| Releases | One public GitHub Release: [`v0.1.0`](https://github.com/rui8001/produce-teaching-video/releases/tag/v0.1.0); the verified `v0.1.1` tag does not yet have a Release page |
| Reproducibility | [Fresh-install verification](./FRESH_INSTALL_TEST.md), a [physics walkthrough](../examples/solar-eclipse/README.md), and a [Git walkthrough](../examples/git-merge-conflict/README.md) |
| Automated maintenance | Latest checked run: [Repository quality #9](https://github.com/rui8001/produce-teaching-video/actions/runs/33495915863), passed |
| Public issue work | Four outcome Issues closed; [real-user trial Issue #2](https://github.com/rui8001/produce-teaching-video/issues/2) remains open |
| Adoption snapshot | 0 stars, 0 forks, 0 recorded real-user invitations, and 0 responses; no adoption claim is made |
| Active history | Dated [evidence log](./CODEX_OSS_APPLICATION.md#evidence-log), roadmap, changelog, tested commits, and release gates |

## Draft: why this repository qualifies

Do not remove the early-adoption sentence unless new public evidence supports the change.

<!-- application-answer:repository_qualification:start -->
```text
Produce Teaching Video is a public MIT-licensed Codex Skill that turns any subject or practical skill into an evidence-based teaching-video workflow. It has reproducible physics and Git examples, clean-install verification, automated privacy and quality checks, versioned artifact validation, and active public maintenance. Adoption is still early: real-user testing is ready, but no real-user usage evidence has been recorded yet.
```
<!-- application-answer:repository_qualification:end -->

## Draft: API-credit use

<!-- application-answer:api_credit_use:start -->
```text
We would use API credits only for this public repository: triaging reproducible issues, evaluating Skill regressions against consent-safe fixtures, reviewing pull requests for artifact-contract and privacy failures, drafting release notes from verified changes, and checking release candidates. Automation would not contact users, publish releases, or submit applications without maintainer approval.
```
<!-- application-answer:api_credit_use:end -->

## Draft: anything else

<!-- application-answer:anything_else:start -->
```text
This repository deliberately excludes private production projects, student or client data, credentials, cookies, paid assets, and fabricated adoption signals. Public examples use official sources, deterministic demonstrations, and self-authored visuals. The v0.2.0 release remains gated on real voluntary user feedback, and the application will not be submitted until its evidence is current.
```
<!-- application-answer:anything_else:end -->

The repository validator enforces the current 500-character limit for each marked draft. Passing that check does not prove that an answer is persuasive, current, or accepted by OpenAI.

## Final submission checklist

1. Reopen the official application and Program Terms; record any changed field or limit before editing the drafts.
2. Refresh repository visibility, releases, CI, Issues, stars, forks, and the consent-safe trial ledger.
3. Replace the early-adoption sentence only with verifiable usage evidence.
4. Confirm the maintainer role, legal name, ChatGPT email, public GitHub profile, and OpenAI Organization ID outside the repository.
5. Confirm the exact benefits requested and that the API-credit plan applies only to repositories the applicant owns, maintains, or is authorized to administer.
6. Remove confidential information; the Program Terms say application materials should not contain it.
7. Have the maintainer review every answer and explicitly authorize submission. Repository automation must not submit the form.
