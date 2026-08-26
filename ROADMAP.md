# Roadmap

This repository is maintained as a subject-agnostic teaching-video Skill. The next public milestone focuses on proving that a new user can install the Skill, reproduce its method, and apply it to more than one subject.

## Two-week public maintenance cycle

**Window:** 2026-08-25 to 2026-09-07  
**Primary outcome:** prepare a credible, evidence-backed Codex for Open Source application without importing private production work.

| Stage | Target | Public evidence | Status |
| --- | --- | --- | --- |
| Foundation | Publish the maintenance plan, evidence checklist, and tester guide | Roadmap and linked GitHub issues | Complete |
| Physics example | Expand the solar-eclipse brief into a reproducible end-to-end walkthrough | [Issue #5](https://github.com/rui8001/produce-teaching-video/issues/5) | Planned |
| Quality automation | Validate the Skill, examples, links, SVG files, and sensitive-data boundaries on every change | [Passing workflow](https://github.com/rui8001/produce-teaching-video/actions/runs/32956656619) | Complete |
| Fresh install | Verify discovery and the five-minute start from a clean checkout | [Issue #3](https://github.com/rui8001/produce-teaching-video/issues/3) | Planned |
| Non-physics example | Demonstrate transfer to a different teaching domain | [Issue #4](https://github.com/rui8001/produce-teaching-video/issues/4) | Planned |
| Real-user trial | Collect voluntary feedback from 3–5 real testers | [Issue #2](https://github.com/rui8001/produce-teaching-video/issues/2) | Planned |
| Release | Publish meaningful fixes as v0.1.1 and the completed milestone as v0.2.0 | Changelog, tags, and release notes | Planned |
| Application pack | Summarize maintenance, usage, ecosystem value, and planned API-credit use | Maintainer-only application checklist | Planned |

Releases are tied to completed outcomes, not to a calendar alone. If a release gate is not met, the release moves rather than publishing an empty version.

## v0.1.1 acceptance criteria

- The solar-eclipse example covers the durable production artifacts, not only the initial brief.
- Automated checks run on pull requests and pushes to `main`.
- Installation and discovery are verified from a clean checkout.
- The README points to the complete example and current maintenance status.
- All tracked files pass the privacy, licensing, link, YAML, JSON, and Skill validation checks.

## v0.2.0 acceptance criteria

- One complete physics example and one complete non-physics example are public.
- At least three real people have been invited to try the Skill, and their actual feedback is recorded without fabrication.
- Confirmed usability problems from the trial are resolved or transparently tracked.
- The Skill remains independent of one subject, presenter, brand, or video framework.
- The release is installable as a standalone Skill and includes clear upgrade notes.

## Maintenance boundaries

- Do not copy files from the author's private production projects into this repository.
- Do not publish student information, account data, credentials, private paths, copyrighted course materials, or client work.
- Use synthetic, public-domain, openly licensed, or self-created demonstration assets.
- Do not manufacture stars, downloads, Issues, pull requests, testimonials, or contributors.
- Human testers choose whether to post publicly. Private feedback may be summarized only with permission and without identifying information.

## Later milestones

- Add optional JSON Schemas for the learning brief, source ledger, visual plan, and production status.
- Add more subject patterns only when real use reveals a reusable teaching need.
- Publish anonymized maintenance retrospectives and upgrade notes.
- Explore API-assisted issue triage, regression evaluation, pull-request review, and release drafting for the open-source project.
