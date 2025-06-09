from fastapi import APIRouter
from app.api.v1 import auth

api_router = APIRouter()

# Include authentication routes
api_router.include_router(auth.router, prefix="/v1")

@api_router.get("/")
async def api_root():
    return {"message": "Finance Tracker API v1"}

@api_router.get("/test")
async def test_endpoint():
    return {
        "status": "success",
        "message": "API is working perfectly!",
        "features": [
            "✅ User authentication",
            "🔄 Account management (coming soon)", 
            "🔄 Transaction tracking (coming soon)",
            "🔄 Budget planning (coming soon)"
        ]
    }
