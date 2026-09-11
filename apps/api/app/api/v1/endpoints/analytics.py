from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.repositories.domain import FinanceOperationsRepository
from app.schemas.analytics import FinanceAnalyticsResponse
from app.services.analytics import FinanceAnalyticsService

router = APIRouter(prefix="/analytics", tags=["Finance Analytics"])

@router.get("", response_model=FinanceAnalyticsResponse)
async def get_analytics(db: AsyncSession = Depends(get_db)):
    repo = FinanceOperationsRepository(db)
    service = FinanceAnalyticsService(repo)
    return await service.get_finance_analytics()
