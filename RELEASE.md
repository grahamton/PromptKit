# Release Checklist

This project follows Keep a Changelog and Semantic Versioning.

1. Verify CI is green on `main` (lint, format, tests).
2. Decide version bump (patch/minor/major) based on changes.
3. Update version in `pyproject.toml` (`[project].version`).
4. Update `CHANGELOG.md`:
   - Move items from `[Unreleased]` under the new version heading with date.
   - Keep `[Unreleased]` present for future work.
5. Commit with a conventional message, e.g. `chore(release): v0.0.X`.
6. Tag the release: `git tag v0.0.X && git push --tags`.
7. (Optional) Build and publish to PyPI:
   - `python -m pip install build twine`
   - `python -m build`
   - `twine upload dist/*`

Notes
- Web app pieces are optional and not part of the CLI package publish.
- Keep core logic pure (no network/fs); CLI handles IO.
