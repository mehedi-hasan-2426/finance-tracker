#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

def main():
    project_root = Path(__file__).parent.parent
    print("🔧 Formatting code...")
    subprocess.run([sys.executable, "-m", "black", "app/", "tests/"], cwd=project_root)
    subprocess.run([sys.executable, "-m", "isort", "app/", "tests/"], cwd=project_root)
    print("✅ Code formatting complete!")

if __name__ == "__main__":
    main()
