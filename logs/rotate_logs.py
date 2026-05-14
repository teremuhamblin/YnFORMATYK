# logs/rotate_logs.py
import os
import time
from pathlib import Path

def rotate_logs():
    base = Path(__file__).resolve().parent
    date = time.strftime("%Y-%m-%d")

    for log_file in base.glob("*.log"):
        archive = base / f"{log_file.stem}.{date}.log"
        if log_file.stat().st_size > 0:
            log_file.rename(archive)
            log_file.touch()
            print(f"[ROTATE] {log_file.name} → {archive.name}")

if __name__ == "__main__":
    rotate_logs()
