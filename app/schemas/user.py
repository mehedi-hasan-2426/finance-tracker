# app/schemas/user.py
from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from .common import TimestampSchema


class UserBase(BaseModel):
    """Base user schema with common fields."""
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr


class UserCreate(UserBase):
    """Schema for creating a new user."""
    password: str = Field(..., min_length=8, max_length=100)


class UserUpdate(BaseModel):
    """Schema for updating user information."""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None


class UserResponse(UserBase, TimestampSchema):
    """Schema for user responses (excludes password)."""
    id: int
    is_active: bool

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    """Schema for user login."""
    username: str
    password: str


class Token(BaseModel):
    """Schema for authentication tokens."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int


