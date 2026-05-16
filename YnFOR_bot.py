# YnFOR_bot.py
from datetime import datetime
from pathlib import Path
import subprocess

REPO_ROOT = Path(__file__).resolve().parent

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def update_docs():
    # Création automatique des dossiers manquants
    docs_dir = REPO_ROOT / "docs" / "plugins"
    docs_dir.mkdir(parents=True, exist_ok=True)

    # Fichier généré automatiquement
    docs_file = docs_dir / "auto_generated_overview.md"
    content = (
        "# Auto‑Generated Overview\n\n"
        f"Dernière mise à jour : {datetime.utcnow().isoformat()}Z\n"
    )
    docs_file.write_text(content, encoding="utf-8")

def commit_changes():
    run('git config user.name "ynfor-bot"')
    run('git config user.email "bot@ynfor.local"')
    run("git add .")
    run('git commit -m "chore(bot): auto-update plugin docs"')

if __name__ == "__main__":
    update_docs()
    commit_changes()
