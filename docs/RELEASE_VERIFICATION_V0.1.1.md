# v0.1.1 release verification

This record verifies the immutable `v0.1.1` tag before the GitHub Release page is published.

## Verified build

- Date: 2026-08-29
- Version: [`v0.1.1`](https://github.com/rui8001/produce-teaching-video/tree/v0.1.1)
- Source commit: [`9616c4b`](https://github.com/rui8001/produce-teaching-video/commit/9616c4bc2f4fcb5036acfc78424e3a5a2c66b325)
- Repository quality: [passed](https://github.com/rui8001/produce-teaching-video/actions/runs/33246893623)

## Checks performed

1. Ran the repository validator in an isolated Python environment; Skill metadata, YAML, JSON, SVG, local links, and sensitive-data checks passed.
2. Ran the official Skill quick validator against the release commit.
3. Confirmed the spoken script, dialogue lines, semantic shot IDs, and audio-unlocked timing state remain consistent.
4. Reviewed the tracked-file inventory and confirmed that only text, JSON, YAML, Python, SVG, license, and Git metadata files are included.
5. Cloned the public `v0.1.1` tag into a new repository-scoped `.agents/skills/produce-teaching-video` directory.
6. Re-ran both validators against the fresh tag checkout and confirmed that Codex exposed the fresh `SKILL.md` path in its model-visible Skill list.
7. Confirmed that the release checkout contains no symbolic links.

All checks passed.

## Release boundary

The annotated Git tag is public and immutable. Publishing the separate GitHub Release page remains pending maintainer confirmation because it posts public release notes on the maintainer's behalf. No private production project, media, account data, credentials, student information, or client content was read or included.
