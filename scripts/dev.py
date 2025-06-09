#!/usr/bin/env python3
"""Development server startup script."""

import subprocess
import sys

def main():
    """Start the development server."""
    cmd = [
        sys.executable, "-m", "uvicorn", 
        "app.main:app", 
        "--reload", 
        "--host", "0.0.0.0", 
        "--port", "8000"
    ]
    subprocess.run(cmd)

if __name__ == "__main__":
    main()
