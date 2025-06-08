# app/schemas/category.py
from pydantic import BaseModel, Field
from typing import Optional
from .common import TimestampSchema


class CategoryGroupBase(BaseModel):
    """Base category group schema."""
    name: str = Field(..., max_length=50)
    type: str = Field(..., regex="^(income|expense|transfer)$")
    description: Optional[str] = Field(None, max_length=255)


class CategoryGroupResponse(CategoryGroupBase):
    """Schema for category group responses."""
    id: int

    class Config:
        from_attributes = True


class CategoryBase(BaseModel):
    """Base category schema."""
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    color: Optional[str] = Field(None, regex="^#[0-9A-Fa-f]{6}$")  # Hex color
    icon: Optional[str] = Field(None, max_length=50)


class CategoryCreate(CategoryBase):
    """Schema for creating categories."""
    category_group_id: int


class CategoryUpdate(BaseModel):
    """Schema for updating categories."""
    name: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    color: Optional[str] = Field(None, regex="^#[0-9A-Fa-f]{6}$")
    icon: Optional[str] = Field(None, max_length=50)
    is_active: Optional[bool] = None


class CategoryResponse(CategoryBase, TimestampSchema):
    """Schema for category responses."""
    id: int
    user_id: int
    category_group_id: int
    is_active: bool
    category_group: CategoryGroupResponse

    class Config:
        from_attributes = True
