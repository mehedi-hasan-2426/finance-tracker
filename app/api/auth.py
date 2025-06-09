from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import UserCreate, UserLogin, UserResponse, Token
from app.services.auth_service import AuthService
from app.services.user_service import UserService
from app.database.connection import get_db

router = APIRouter(prefix="/auth", tags=["authentication"])
security = HTTPBearer()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    """Register a new user."""
    user_service = UserService(db)
    
    # Check if user already exists
    existing_user = await user_service.get_user_by_username(user_data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    
    existing_email = await user_service.get_user_by_email(user_data.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    new_user = await user_service.create_user(user_data)
    return new_user

@router.post("/login", response_model=Token)
async def login_user(
    login_data: UserLogin,
    db: AsyncSession = Depends(get_db)
):
    """Login user and return access token."""
    user_service = UserService(db)
    auth_service = AuthService()
    
    # Verify user credentials
    user = await user_service.authenticate_user(login_data.username, login_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Create access token
    access_token = auth_service.create_access_token({"sub": user.username})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": 1800  # 30 minutes
    }

@router.get("/me", response_model=UserResponse)
async def get_current_user_info(
    current_user = Depends(get_current_user),
):
    """Get current user information."""
    return current_user
