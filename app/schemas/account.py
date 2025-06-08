# app/schemas/account.py
from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from .common import TimestampSchema


class AccountTypeBase(BaseModel):
    """Base account type schema."""
    name: str = Field(..., max_length=50)
    description: Optional[str] = Field(None, max_length=255)


class AccountTypeCreate(AccountTypeBase):
    """Schema for creating account types."""
    pass


class AccountTypeResponse(AccountTypeBase):
    """Schema for account type responses."""
    id: int

    class Config:
        from_attributes = True


class AccountBase(BaseModel):
    """Base account schema."""
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    initial_balance: Decimal = Field(default=0, ge=0)
    currency: str = Field(default="USD", max_length=3)


class AccountCreate(AccountBase):
    """Schema for creating accounts."""
    account_type_id: int


class AccountUpdate(BaseModel):
    """Schema for updating accounts."""
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    is_active: Optional[bool] = None


class AccountResponse(AccountBase, TimestampSchema):
    """Schema for account responses."""
    id: int
    user_id: int
    account_type_id: int
    current_balance: Decimal
    is_active: bool
    account_type: AccountTypeResponse

    class Config:
        from_attributes = True

