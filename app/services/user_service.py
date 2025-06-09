from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User
from app.schemas.user import UserCreate
from app.services.auth_service import AuthService

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.auth_service = AuthService()

    async def get_user_by_username(self, username: str) -> Optional[User]:
        """Get user by username."""
        result = await self.db.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """Get user by email."""
        result = await self.db.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def create_user(self, user_data: UserCreate) -> User:
        """Create a new user."""
        # Hash the password
        hashed_password = self.auth_service.hash_password(user_data.password)
        
        # Create user object
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=hashed_password
        )
        
        # Save to database
        self.db.add(new_user)
        await self.db.commit()
        await self.db.refresh(new_user)
        
        return new_user

    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Authenticate user credentials."""
        user = await self.get_user_by_username(username)
        if not user:
            return None
            
        if not self.auth_service.verify_password(password, user.password_hash):
            return None
            
        return user
