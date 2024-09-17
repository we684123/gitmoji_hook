import sys
from pathlib import Path


def add_merge_prefix(commit_msg_file: str) -> None:
    # 檢查是否處於合併衝突狀態
    print("Checking for merge conflict...")
    merge_head = Path(".git/MERGE_HEAD")
    if merge_head.exists():
        print("Merge conflict detected, skipping commit message modification.")
        return

    # 讀取 commit 訊息檔案的路徑
    commit_msg_path = Path(commit_msg_file)

    try:
        commit_msg = commit_msg_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Error: Commit message file '{commit_msg_file}' not found.")
        sys.exit(1)

    # 如果 commit 訊息包含 "Merge branch"，且未加上表情符號，則加上 "🔀 "
    if "Merge branch" in commit_msg and not commit_msg.startswith("🔀"):
        new_commit_msg = "🔀 " + commit_msg
        commit_msg_path.write_text(new_commit_msg, encoding="utf-8")
        print("Modified commit message:")
        print(new_commit_msg)  # 顯示修改後的 commit 訊息
    else:
        print("No modifications made to commit message.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No commit message file path provided.")
        sys.exit(1)

    # 接收 commit 訊息檔案的路徑作為參數
    commit_msg_file = sys.argv[1]
    print(f"Commit message file path: {commit_msg_file}")  # 調試訊息

    add_merge_prefix(commit_msg_file)
