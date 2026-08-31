# Real-user testing guide

This trial checks whether a new user can install and use the Skill without help from its author. It is not a request for stars, promotion, a public identity, or artificial GitHub activity.

**Trial status on 2026-08-31:** the testing kit is ready; no invitations, accepted volunteers, or completed trials have been recorded. Maintainer self-tests do not count as real-user evidence.

- Maintainers can start with the [voluntary invitation template](./USER_TEST_INVITATION.md).
- Testers can return the [anonymous feedback template](./USER_TEST_FEEDBACK_TEMPLATE.md) privately or use the optional [GitHub usability-report form](https://github.com/rui8001/produce-teaching-video/issues/new?template=usability_report.yml).
- Only consented, anonymous aggregate results belong in the [public results ledger](./USER_TEST_RESULTS.md).

## Who can test

Any teacher, tutor, knowledge creator, course designer, or beginner exploring instructional video production can participate. Coding experience is not required. Participation is voluntary, and a tester may stop at any time without giving a reason.

## Before the trial

1. Use a small public or synthetic topic that the tester already understands. Do not use student data, client work, unpublished course content, private repositories, credentials, account details, or copyrighted source files.
2. Start with the repository README. The maintainer should not provide extra installation or workflow coaching until the tester reaches their first blocker.
3. Choose one route:
   - **Route A — discovery check (5–10 minutes):** install the Skill and confirm that Codex can invoke `$produce-teaching-video`.
   - **Route B — first-use task (20–30 minutes):** complete Route A, then request a learning brief, source ledger, and initial visual plan.
4. Stop before paid services, external uploads, publishing, voice generation, or full rendering. A finished video is not required.

OpenAI's [Build skills guide](https://learn.chatgpt.com/docs/build-skills) documents repository and personal Skill locations, explicit `$` invocation, automatic discovery, and restarting Codex if a new Skill does not appear.

## Run sheet

### Route A — discovery check

1. Start from a Codex environment where this Skill is not already installed.
2. Follow the README installation instructions without maintainer help.
3. Confirm that `produce-teaching-video` appears as an available Skill or can be explicitly invoked with `$produce-teaching-video`.
4. Record one outcome: `completed`, `completed_with_help`, `blocked_install`, `blocked_discovery`, or `stopped_by_choice`.
5. If blocked, record the first failed step and the exact non-sensitive error text. Do not troubleshoot it away before capturing the first attempt.

### Route B — first-use task

After Route A succeeds, replace the placeholders in this prompt:

```text
$produce-teaching-video 把“<一个公开或虚构的小主题>”规划成一条面向<受众>的教学视频。请只完成学习简报、来源台账和初始视觉计划；明确标记缺失来源、假设和模型边界，并停在任何付费、外部上传、配音或渲染之前。
```

Observe the first response without asking the maintainer what a good result should look like. Check whether it:

- states one audience and one observable learning objective;
- identifies likely prior knowledge and a misconception or failure point;
- separates supported facts, missing sources, assumptions, and model limits;
- proposes a visual explanation rather than decorative footage alone;
- names the next checkpoint and does not silently cross paid, account, upload, publishing, or rendering boundaries.

Record one outcome: `completed`, `completed_with_help`, `blocked_invoke`, `blocked_workflow`, or `stopped_by_choice`. A trial still counts as evidence when it fails, provided the failure is recorded truthfully.

## Feedback and consent

Use the [feedback template](./USER_TEST_FEEDBACK_TEMPLATE.md) to record the first confusing step, the first blocker, what worked, and whether the tester would reuse the workflow. Test IDs such as `T01` replace names and email addresses.

- Opening a GitHub Issue reveals the tester's GitHub account. Use private feedback if that is not wanted.
- Private feedback is not published or quoted by default.
- The maintainer may add an anonymous summary to the results ledger only when the tester explicitly allows it.
- A public Issue may be opened or linked to the trial only with the tester's permission.
- No permission is inferred from silence, participation, or a completed test.

## Maintainer triage

Classify the first confirmed problem before proposing a fix:

- **Blocker:** the Skill cannot be installed or invoked, or it crosses an authorization/privacy boundary.
- **Major:** the tester cannot identify the learning goal, evidence gap, visual explanation, or next safe step.
- **Minor:** the workflow completes, but wording, navigation, or an optional artifact causes avoidable friction.

Record failed and successful trials alike in the [results ledger](./USER_TEST_RESULTS.md). The v0.2.0 gate remains closed until at least three real people have been invited and confirmed usability problems are resolved or transparently tracked.
