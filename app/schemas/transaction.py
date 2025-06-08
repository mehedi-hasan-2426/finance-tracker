# app/schemas/transaction.py
from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from datetime import date
from .common import TimestampSchema
from .account import AccountResponse
from .category import CategoryResponse


class TransactionBase(BaseModel):
    """Base transaction schema."""
    amount: Decimal = Field(..., decimal_places=2)
    description: str = Field(..., max_length=255)
    transaction_date: date
    notes: Optional[str] = None
    reference_number: Optional[str] = Field(None, max_length=100)


class TransactionCreate(TransactionBase):
    """Schema for creating transactions."""
    account_id: int
    category_id: int


class TransactionUpdate(BaseModel):
    """Schema for updating transactions."""
    amount: Optional[Decimal] = Field(None, decimal_places=2)
    description: Optional[str] = Field(None, max_length=255)
    transaction_date: Optional[date] = None
    category_id: Optional[int] = None
    notes: Optional[str] = None
    reference_number: Optional[str] = Field(None, max_length=100)


class TransactionResponse(TransactionBase, TimestampSchema):
    """Schema for transaction responses."""
    id: int
    user_id: int
    account_id: int
    category_id: int
    is_recurring: bool
    account: AccountResponse
    category: CategoryResponse

    class Config:
        from_attributes = True


class TransactionListResponse(BaseModel):
    """Schema for paginated transaction lists."""
    transactions: list[TransactionResponse]
    total: int
    page: int
    size: int
    pages: int
