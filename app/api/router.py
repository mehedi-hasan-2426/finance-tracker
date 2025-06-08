from fastapi import APIRouter

api_router = APIRouter()

# Import and include individual routers
# from app.api.v1 import auth, accounts, transactions, categories, budgets

@api_router.get("/")
async def api_root():
    return {"message": "Finance Tracker API v1"}
