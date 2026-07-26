# gitmoji_hook

[![Gitmoji](https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square)](https://gitmoji.dev)

Git hook with [Gitmoji](https://gitmoji.dev/)

## Features

1. Change merge commit messages to Gitmoji style.
   ![2024-07-25 00_23_32-2024-07-24 23_51_41-Greenshot png](https://github.com/user-attachments/assets/81d864ee-8adf-419b-8819-dab368f91882)
2. The hook uses only the shell already expected by `language: script`; it does not install a hook-specific runtime or package.

## Remote installation with pre-commit

Install `pre-commit` once if it is not already available. Then add this repository as a normal remote hook in your project's `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
        exclude: \.md$
      - id: check-added-large-files
      - id: check-case-conflict
      - id: check-json
      - id: check-toml
      - id: check-yaml
      - id: end-of-file-fixer

  - repo: https://github.com/we684123/gitmoji_hook
    rev: v0.2.0
    hooks:
      - id: gitmoji-merge-commit-msg
```

Install the `prepare-commit-msg` hook type and then commit normally:

```bash
pre-commit install --hook-type prepare-commit-msg
```

The `🔀` Gitmoji is added when Git generates a merge message beginning with `Merge branch`. This follows the Gitmoji convention for merging branches; see [gitmoji.dev](https://gitmoji.dev/).

## Local verification

To verify the online hook in a fresh repository:

```bash
git init
pre-commit install --hook-type prepare-commit-msg
git checkout -b feature
git checkout main
git merge --no-ff feature
git log -1 --format=%s
```

The final subject should begin with `🔀 Merge branch`.
