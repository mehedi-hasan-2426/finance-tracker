#!/usr/bin/env python3
import subprocess
import sys

def main():
    cmd = [sys.executable, "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
