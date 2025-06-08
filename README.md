# Finance Tracker

A personal finance tracking application built with FastAPI and SQLAlchemy.

## Features

- Track income and expenses
- Categorize transactions
- Budget management
- Account management (checking, savings, credit cards)
- Financial reports and analytics

## Quick Start

1. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

3. Run the development server:
   ```bash
   poetry run dev
   ```

4. Open your browser to `http://localhost:8000/docs` to see the API documentation.

## Development

### Running Tests
```bash
poetry run test
```

### Code Formatting
```bash
poetry run format
```

### Code Linting
```bash
poetry run lint
```

### Database Migrations
```bash
poetry run alembic revision --autogenerate -m "Description"
poetry run alembic upgrade head
```

## Project Structure

```
finance-tracker/
├── app/                    # Main application code
│   ├── api/               # API endpoints
│   ├── core/              # Core functionality
│   ├── models/            # Database models
│   ├── schemas/           # Pydantic schemas
│   ├── services/          # Business logic
│   └── database/          # Database configuration
├── tests/                 # Test suite
├── docs/                  # Documentation
└── scripts/               # Utility scripts
```

## License

MIT License
