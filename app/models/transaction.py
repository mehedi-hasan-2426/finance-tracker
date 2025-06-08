# app/models/transaction.py
from sqlalchemy import String, Numeric, Date, ForeignKey, Boolean, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from datetime import date
from .base import Base, TimestampMixin


class Transaction(Base, TimestampMixin):
    """Main transactions table."""
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), index=True)
    amount: Mapped[Decimal] = mapped_column(Numeric(12, 2))
    description: Mapped[str] = mapped_column(String(255))
    transaction_date: Mapped[date] = mapped_column(Date, index=True)
    notes: Mapped[str] = mapped_column(Text, nullable=True)
    reference_number: Mapped[str] = mapped_column(String(100), nullable=True)
    is_recurring: Mapped[bool] = mapped_column(Boolean, default=False)

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="transactions")
    account: Mapped["Account"] = relationship("Account", back_populates="transactions")
    category: Mapped["Category"] = relationship("Category", back_populates="transactions")
