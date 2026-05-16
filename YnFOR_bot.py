# ynfor_bot.py
import subprocess
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def update_docs():
    docs_file = REPO_ROOT / "docs" / "plugins" / "auto_generated_overview.md"
    content = f"# Auto‑Generated Overview\n\nDernière mise à jour : {datetime.utcnow().isoformat()}Z\n"
    docs_file.write_text(content, encoding="utf-8")

def commit_changes():
    run('git config user.name "ynfor-bot"')
    run('git config user.email "bot@ynfor.local"')
    run("git add .")
    run('git commit -m "chore(bot): auto-update plugin docs"')

if __name__ == "__main__":
    update_docs()
    commit_changes()
