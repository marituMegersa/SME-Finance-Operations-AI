from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.api.deps import get_db
from app.schemas.domain import UnderwritingEvalRequest, UnderwritingEvalResponse
from app.repositories.domain import FinanceOperationsRepository
from app.services.domain import FinanceOperationsService

router = APIRouter(prefix="/finance", tags=["Credit Underwriting & Cash Flow"])

def get_service(db: AsyncSession = Depends(get_db)) -> FinanceOperationsService:
    repo = FinanceOperationsRepository(db)
    return FinanceOperationsService(repo)

@router.post("/underwrite", response_model=UnderwritingEvalResponse, status_code=status.HTTP_201_CREATED)
async def evaluate_underwriting(req: UnderwritingEvalRequest, service: FinanceOperationsService = Depends(get_service)):
    return await service.evaluate_underwriting(req)

@router.get("/ledger")
async def list_ledger(skip: int = Query(0, ge=0), limit: int = Query(50, le=100), service: FinanceOperationsService = Depends(get_service)):
    return await service.list_ledger(skip=skip, limit=limit)
