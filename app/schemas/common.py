# app/schemas/common.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TimestampSchema(BaseModel):
    """Base schema with timestamp fields."""
    created_at: datetime
    updated_at: datetime


class ResponseSchema(BaseModel):
    """Standard API response schema."""
    success: bool = True
    message: str = "Operation successful"
    data: Optional[dict] = None



