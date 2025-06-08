from fastapi import FastAPI
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
    return {"status": "healthy"}
