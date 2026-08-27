# Fresh-install verification

This record verifies that the public repository can be installed and discovered as a standalone Codex Skill without credentials, paid services, or access to the author's production projects.

## Verified build

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

All checks passed.

## Onboarding correction

The test found that the initial README used the older `~/.codex/skills` personal path. The installation instructions now use the current documented user location, `~/.agents/skills`, while retaining `.agents/skills` for project-scoped installation.

## What this proves

- The GitHub repository can be downloaded without authentication.
- The root package is structurally valid as one standalone Skill.
- Codex can discover the installed Skill from the documented directory.
- Explicit invocation with `$produce-teaching-video` is represented correctly in the discovered metadata.

This test does not claim that every teaching-video task will succeed. Subject accuracy, source quality, production tools, and learner outcomes require separate example and real-user testing.
