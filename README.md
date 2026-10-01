# Finance Tracker

A personal finance API built with FastAPI, async SQLAlchemy, and Alembic.

**Status: early work in progress.** This is a learning project I started to practise building a Python backend. It does not run yet in its current state, and most features are planned rather than built.

## What exists

- Database models for users, accounts, account types, categories, category groups, and transactions
- Pydantic schemas for those models
- Auth endpoints for register, login, and the current user (`app/api/auth.py`)
- Account endpoints to create and list accounts (`app/api/v1/accounts.py`)
- A pytest setup with three smoke tests for the root, health, and API root endpoints
- Alembic configuration for migrations

## Known issues

- The router imports `auth` from `app.api.v1`, but the module lives at `app/api/auth.py`, so the app fails on import.
- The account endpoints are not registered with the router.
- There is a leftover duplicate of the project in the nested `finance-tracker/` folder.

## Planned

- Recording income and expenses
- Budgets
- Reports

## Running it

Install dependencies with [Poetry](https://python-poetry.org/):

```bash
poetry install
```

Once the import issue above is fixed, start the server with:

```bash
poetry run uvicorn app.main:app --reload
```

Then open `http://localhost:8000/docs`.

Run the tests with:

```bash
poetry run pytest
```

## License

MIT License
