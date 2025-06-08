#!/bin/bash

# Safe Finance Tracker Project Setup Script
# This version checks for existing files and asks before overwriting

echo "🔍 Checking for existing Finance Tracker project..."

# Check if directory exists
if [ -d "finance-tracker" ]; then
    echo "⚠️  finance-tracker directory already exists!"
    echo "Choose an option:"
    echo "1) Backup existing and create fresh (recommended)"
    echo "2) Add only missing files to existing project"
    echo "3) Cancel and exit"
    read -p "Enter your choice (1/2/3): " choice
    
    case $choice in
        1)
            echo "📦 Creating backup..."
            if [ -d "finance-tracker-backup" ]; then
                echo "Backup already exists. Creating timestamped backup..."
                cp -r finance-tracker "finance-tracker-backup-$(date +%Y%m%d-%H%M%S)"
            else
                cp -r finance-tracker finance-tracker-backup
            fi
            echo "✅ Backup created as finance-tracker-backup"
            rm -rf finance-tracker
            ;;
        2)
            echo "📁 Adding only missing files..."
            cd finance-tracker
            EXISTING_PROJECT=true
            ;;
        3)
            echo "❌ Setup cancelled."
            exit 0
            ;;
        *)
            echo "❌ Invalid choice. Exiting."
            exit 1
            ;;
    esac
else
    echo "✅ No existing project found. Creating fresh project..."
    EXISTING_PROJECT=false
fi

# Function to create file only if it doesn't exist
create_file_if_missing() {
    local file_path="$1"
    local content="$2"
    
    if [ ! -f "$file_path" ]; then
        echo "📝 Creating $file_path"
        echo "$content" > "$file_path"
    else
        echo "⏭️  Skipping $file_path (already exists)"
    fi
}

# Function to create directory only if it doesn't exist
create_dir_if_missing() {
    local dir_path="$1"
    
    if [ ! -d "$dir_path" ]; then
        echo "📁 Creating directory $dir_path"
        mkdir -p "$dir_path"
    else
        echo "⏭️  Directory $dir_path already exists"
    fi
}

# Create main project directory if not in existing project mode
if [ "$EXISTING_PROJECT" != "true" ]; then
    mkdir -p finance-tracker
    cd finance-tracker
fi

echo "🏗️  Setting up project structure..."

# Create directory structure
directories=(
    "app" "app/api" "app/api/v1" "app/core" "app/services"
    "app/models" "app/schemas" "app/database" "app/database/migrations"
    "app/database/migrations/versions" "app/repositories" "app/utils"
    "tests" "tests/unit" "tests/unit/test_services" "tests/unit/test_repositories" 
    "tests/unit/test_utils" "tests/integration" "tests/integration/test_api"
    "tests/integration/test_database" "tests/fixtures"
    "scripts" "docs" "docs/api" "docs/deployment" "docs/development"
    "deployment" "deployment/docker" "deployment/kubernetes" "deployment/systemd"
    "frontend" "frontend/static" "frontend/templates" "frontend/src"
)

for dir in "${directories[@]}"; do
    create_dir_if_missing "$dir"
done

# Create __init__.py files
init_files=(
    "app/__init__.py" "app/api/__init__.py" "app/api/v1/__init__.py"
    "app/core/__init__.py" "app/services/__init__.py" "app/models/__init__.py"
    "app/schemas/__init__.py" "app/database/__init__.py" "app/repositories/__init__.py"
    "app/utils/__init__.py" "tests/__init__.py" "tests/unit/__init__.py"
    "tests/integration/__init__.py" "tests/fixtures/__init__.py"
)

for init_file in "${init_files[@]}"; do
    create_file_if_missing "$init_file" ""
done

# Create configuration files
create_file_if_missing "pyproject.toml" '[tool.poetry]
name = "finance-tracker"
version = "0.1.0"
description = "Personal Finance Tracking Application"
authors = ["Your Name <your.email@example.com>"]
license = "MIT"
readme = "README.md"
keywords = ["finance", "budget", "tracking", "fastapi"]
packages = [{include = "app"}]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.104.0"
uvicorn = {extras = ["standard"], version = "^0.24.0"}
sqlalchemy = "^2.0.0"
alembic = "^1.12.0"
pydantic = "^2.4.0"
pydantic-settings = "^2.0.0"
python-jose = {extras = ["cryptography"], version = "^3.3.0"}
python-multipart = "^0.0.6"
bcrypt = "^4.0.0"
python-dotenv = "^1.0.0"
aiosqlite = "^0.19.0"
asyncpg = "^0.29.0"
pandas = "^2.1.0"
httpx = "^0.25.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.4.0"
pytest-asyncio = "^0.21.0"
pytest-cov = "^4.1.0"
black = "^23.0.0"
isort = "^5.12.0"
flake8 = "^6.0.0"
mypy = "^1.5.0"
pre-commit = "^3.4.0"
factory-boy = "^3.3.0"

[[tool.poetry.source]]
name = "pypi"
url = "https://pypi.org/simple/"
priority = "primary"

[[tool.poetry.source]]
name = "pypi-files"
url = "https://files.pythonhosted.org/simple/"
priority = "supplemental"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v --cov=app --cov-report=html"
asyncio_mode = "auto"

[tool.black]
line-length = 88
target-version = ["py311"]

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true'

# Create environment files (only if they don't exist)
create_file_if_missing ".env.example" 'DATABASE_URL=sqlite:///./finance_tracker.db
SECRET_KEY=your-secret-key-here-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP_NAME=Finance Tracker
DEBUG=True
VERSION=0.1.0
ALLOWED_ORIGINS=["http://localhost:3000"]'

# Don't overwrite .env if it exists (it might have real secrets)
if [ ! -f ".env" ]; then
    echo "📝 Creating .env from template"
    cp .env.example .env
else
    echo "⏭️  Skipping .env (already exists - preserving your settings)"
fi

# Create main application files
create_file_if_missing "app/main.py" 'from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.router import api_router

def create_application() -> FastAPI:
    application = FastAPI(
        title=settings.APP_NAME,
        version=settings.VERSION,
        debug=settings.DEBUG,
    )
    
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    application.include_router(api_router, prefix="/api")
    return application

app = create_application()

@app.get("/")
async def root():
    return {"message": "Finance Tracker API", "version": settings.VERSION}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}'

create_file_if_missing "app/config.py" 'from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./finance_tracker.db"
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    APP_NAME: str = "Finance Tracker"
    DEBUG: bool = False
    VERSION: str = "0.1.0"
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()'

create_file_if_missing "app/api/router.py" 'from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/")
async def api_root():
    return {"message": "Finance Tracker API v1"}'

# Create utility scripts
create_file_if_missing "scripts/dev.py" '#!/usr/bin/env python3
import subprocess
import sys

def main():
    cmd = [sys.executable, "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
    subprocess.run(cmd)

if __name__ == "__main__":
    main()'

create_file_if_missing "scripts/format.py" '#!/usr/bin/env python3
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
    main()'

# Make scripts executable
chmod +x scripts/*.py 2>/dev/null || true

# Create .gitignore
create_file_if_missing ".gitignore" '__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
.pytest_cache/
.coverage
htmlcov/
.mypy_cache/
.idea/
.vscode/
*.db
*.sqlite
*.sqlite3
finance_tracker.db'

echo ""
echo "✅ Project setup complete!"
echo ""
if [ "$EXISTING_PROJECT" = "true" ]; then
    echo "📁 Missing files have been added to your existing project."
else
    echo "🎉 New project created successfully!"
fi
echo ""
echo "Next steps:"
echo "1. cd finance-tracker"
echo "2. poetry install"
echo "3. poetry run python scripts/dev.py"
echo ""
echo "The API will be available at: http://localhost:8000"
