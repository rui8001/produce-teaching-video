# Fresh-install verification

This record verifies that the public repository can be installed and discovered as a standalone Codex Skill without credentials, paid services, or access to the author's production projects.

## Current-main recheck

- Date: 2026-09-03
- Source commit: [`3bb2896`](https://github.com/rui8001/produce-teaching-video/commit/3bb28965644a72b772f9290c195fa59ed09a5ebb)
- Host: macOS
- Codex CLI: `0.152.1`
- Install scope: isolated temporary `.agents/skills/produce-teaching-video`

### Procedure and result

1. Installed the root Skill directly from public GitHub `main` with the bundled Skill Installer helper into a new temporary project-scoped Skill directory.
2. Independently shallow-cloned public `main` at the commit above into a correctly named `produce-teaching-video` directory.
3. Confirmed that the installer output and fresh checkout were byte-for-byte identical, excluding only the checkout's `.git` metadata.
4. Ran the official Skill quick validator against the installer output; it passed.
5. Ran the repository validator against the fresh checkout; Skill metadata, schemas, examples, local links, application drafts, SVG, and sensitive-data checks passed.
6. Parsed `agents/openai.yaml` and verified the display name, `$produce-teaching-video` default prompt, implicit-invocation policy, and both icon targets.
7. Ran `codex debug prompt-input` from the isolated project and confirmed that Codex exposed the installed Skill name and description to the model-visible input.
8. Confirmed that the installed package contained zero symbolic links.

All final checks passed. An initial scratch checkout named `checkout` was rejected by the repository validator because the validator intentionally requires the repository folder name to match the Skill name. Re-running the unchanged public commit under the correct package name passed; this was a test-harness path correction, not a package change.

## Original baseline

- Date: 2026-08-27
- Source commit: [`6f6e537`](https://github.com/rui8001/produce-teaching-video/commit/6f6e537708e87c26ff7536705e444cfb7395b15b)
- Host: macOS
- Codex CLI: `0.150.0-alpha.8`
- Install scope: isolated temporary `.agents/skills/produce-teaching-video`

The location follows the current [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills), which lists `$HOME/.agents/skills` for user-scoped skills and `.agents/skills` for repository-scoped skills.

## Checks performed

1. Downloaded the public GitHub repository with the built-in Skill Installer helper into a new temporary `.agents/skills` directory.
2. Confirmed that `SKILL.md`, `agents/openai.yaml`, both icons, all four references, and the public example were present.
3. Ran the official Skill quick validator against the downloaded copy.
4. Parsed the UI metadata and confirmed the skill name, description, explicit invocation prompt, automatic-invocation policy, and icon targets.
5. Ran `codex debug prompt-input` from the isolated directory and confirmed that Codex included `produce-teaching-video` and its temporary `SKILL.md` path in the model-visible skills list.
6. Confirmed that the downloaded package contained no symbolic links.

All baseline checks passed.

## Onboarding correction

The test found that the initial README used the older `~/.codex/skills` personal path. The installation instructions now use the current documented user location, `~/.agents/skills`, while retaining `.agents/skills` for project-scoped installation.

## What this proves

- The GitHub repository can be downloaded without authentication.
- The root package is structurally valid as one standalone Skill.
- Codex can discover the installed Skill from the documented directory.
- Explicit invocation with `$produce-teaching-video` is represented correctly in the discovered metadata.

This test does not claim that every teaching-video task will succeed. Subject accuracy, source quality, production tools, and learner outcomes require separate example and real-user testing.
