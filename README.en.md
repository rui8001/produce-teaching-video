# Produce Teaching Video

An installable Codex Skill for turning any subject or practical skill into an instructional video that changes what a learner can explain or do.

It centers one learning objective, verified sources, a visible mental model, continuous narration, real-audio timing, a representative sample, and a transfer task. Physics animation is one use case—not the boundary of the Skill.

## Install

Recommended: ask Codex to use its built-in installer.

```text
$skill-installer Install the Skill from https://github.com/rui8001/produce-teaching-video.
```

Manual user-scoped installation:

```bash
git clone https://github.com/rui8001/produce-teaching-video.git \
  ~/.agents/skills/produce-teaching-video
```

For repository-scoped use, clone it to `.agents/skills/produce-teaching-video/` inside that repository. Codex normally detects the new Skill automatically; restart Codex if it does not appear. See the [fresh-install verification](./docs/FRESH_INSTALL_TEST.md) for the tested environment and result.

Invoke it with:

```text
$produce-teaching-video Teach why a solar eclipse does not happen every month.
```

See the full [Chinese README](./README.md), the [Skill entrypoint](./SKILL.md), and two cross-domain public examples: [solar-eclipse reasoning](./examples/solar-eclipse/README.md) and [Git merge-conflict resolution](./examples/git-merge-conflict/README.md).
