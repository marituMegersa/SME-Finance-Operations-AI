from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional
from app.api.deps import get_db
from app.repositories.domain import FinanceOperationsRepository
from app.schemas.search import PaginatedFinanceResponse, UnderwritingEvalResponse

router = APIRouter(prefix="/search", tags=["Search & Filter"])

@router.get("", response_model=PaginatedFinanceResponse)
async def search_underwriting(
    min_dscr: Optional[float] = Query(None),
    status: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    db: AsyncSession = Depends(get_db)
):
    repo = FinanceOperationsRepository(db)
    all_recs = await repo.get_multi(skip=(page - 1) * page_size, limit=page_size)
    items = [
        UnderwritingEvalResponse(
            enterprise_id=r.enterprise_id,
            monthly_net_cash_flow=r.monthly_revenue - r.monthly_expenses,
            dscr_ratio=r.dscr_ratio,
            underwriting_status=r.underwriting_status,
            max_credit_facility=250000.0,
            evaluated_at=r.created_at
        ) for r in all_recs
    ]
    return PaginatedFinanceResponse(
        items=items,
        total=len(items),
        page=page,
        page_size=page_size,
        total_pages=1
    )
