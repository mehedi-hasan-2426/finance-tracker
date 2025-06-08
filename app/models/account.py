# app/models/account.py
from sqlalchemy import String, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from decimal import Decimal
from .base import Base, TimestampMixin


class AccountType(Base):
    """Account types (checking, savings, credit card, etc.)."""
    __tablename__ = "account_types"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    # Relationships
    accounts: Mapped[list["Account"]] = relationship("Account", back_populates="account_type")


class Account(Base, TimestampMixin):
    """User accounts (bank accounts, credit cards, etc.)."""
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    account_type_id: Mapped[int] = mapped_column(ForeignKey("account_types.id"))
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    initial_balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)
    current_balance: Mapped[Decimal] = mapped_column(Numeric(12, 2), default=0)
    currency: Mapped[str] = mapped_column(String(3), default="USD")
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="accounts")
    account_type: Mapped["AccountType"] = relationship("AccountType", back_populates="accounts")
    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", back_populates="account", cascade="all, delete-orphan"
    )
