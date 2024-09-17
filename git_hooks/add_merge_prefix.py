import sys
from pathlib import Path


def add_merge_prefix(commit_msg_file: str) -> None:
    # 檢查是否處於合併衝突狀態
    print("Checking for merge conflict...")
    merge_head = Path(".git/MERGE_HEAD")
    if merge_head.exists():
        print("Merge conflict detected, skipping commit message modification.")
        return

    # 讀取 commit 訊息
    commit_msg_path = Path(commit_msg_file)
    commit_msg = commit_msg_path.read_text(encoding="utf-8")

    # 如果 commit 訊息包含 "Merge branch"，則加上 "🔀 "
    if "Merge branch" in commit_msg and not commit_msg.startswith("🔀"):
        new_commit_msg = "🔀 " + commit_msg
        commit_msg_path.write_text(new_commit_msg, encoding="utf-8")
        print("Modified commit message:")
    else:
        print("No modifications made to commit message.")


if __name__ == "__main__":
    # 接收 commit 訊息檔案的路徑作為參數
    commit_msg_file = sys.argv[1]
    add_merge_prefix(commit_msg_file)
