# gitmoji_hook

<p align="left">
    <a href="https://gitmoji.dev">
        <img src="https://img.shields.io/badge/gitmoji-%20😜%20😍-FFDD67.svg?style=flat-square"
             alt="Gitmoji">
    </a>
</p>

Git hook with [Gitmoji](https://gitmoji.dev/)

## features


1. change merge commit message to gitmoji style
   ![2024-07-25 00_23_32-2024-07-24 23_51_41-Greenshot png](https://github.com/user-attachments/assets/81d864ee-8adf-419b-8819-dab368f91882)
2. ~~check commit message with gitmoji style~~ (not yet)

## install by file

copy this repo `./git_hooks/*` (or choose u need) to you repo folder `.git/hooks/` and make it executable.

## install by [pre-commit](https://pre-commit.com/)

1. make sure you have pre-commit installed

    ```bash
    pip install pre-commit
    ```

2. add or update you `.pre-commit-config.yaml` to you repo root folder

    ```yaml
    repos:
    - repo: https://github.com/we684123/gitmoji_hook
        rev: v0.1.0
        hooks:
        - id: gitmoji-merge-commit-msg
    ```

3. install gitmoji_hook

    ```bash
    pre-commit install --hook-type prepare-commit-msg
    ```
