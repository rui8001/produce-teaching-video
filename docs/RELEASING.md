# Release checklist

1. Confirm the release changes only the reusable teaching method and contains no production media or private data.
2. Install `requirements-dev.txt` in an isolated environment and run `python scripts/validate_repository.py`.
3. Run the official Skill validator against the repository root.
4. Confirm the GitHub Actions `Repository quality` check passes for the release commit.
5. Review `git diff` and the tracked-file inventory for copyrighted material or context-specific private content that pattern scans cannot identify.
6. Update `CHANGELOG.md` with the release date and migration notes.
7. Commit with the public no-reply author, create an annotated `vX.Y.Z` tag, and publish release notes from the changelog.
8. Install from a fresh clone and verify that Codex discovers the Skill.
