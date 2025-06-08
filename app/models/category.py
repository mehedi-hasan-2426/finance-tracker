# app/models/category.py
from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, TimestampMixin


class CategoryGroup(Base):
    """Category groups (Income, Expenses, Transfers)."""
    __tablename__ = "category_groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    type: Mapped[str] = mapped_column(String(20))  # income, expense, transfer
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    # Relationships
    categories: Mapped[list["Category"]] = relationship("Category", back_populates="category_group")


class Category(Base, TimestampMixin):
    """Transaction categories."""
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    category_group_id: Mapped[int] = mapped_column(ForeignKey("category_groups.id"))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    color: Mapped[str] = mapped_column(String(7), nullable=True)  # Hex color
    icon: Mapped[str] = mapped_column(String(50), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="categories")
    category_group: Mapped["CategoryGroup"] = relationship("CategoryGroup", back_populates="categories")
    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", back_populates="category", cascade="all, delete-orphan"
    )
