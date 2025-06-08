# app/api/v1/accounts.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.connection import get_db
from app.schemas.account import AccountCreate, AccountResponse
from app.services.account_service import AccountService

router = APIRouter(prefix="/accounts", tags=["accounts"])

@router.post("/", response_model=AccountResponse)
async def create_account(
    account_data: AccountCreate,
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)  # Add auth dependency
):
    service = AccountService(db)
    return await service.create_account(account_data, current_user.id)

@router.get("/", response_model=List[AccountResponse])
async def get_accounts(
    db: AsyncSession = Depends(get_db),
    current_user = Depends(get_current_user)
):
    service = AccountService(db)
    return await service.get_user_accounts(current_user.id)
