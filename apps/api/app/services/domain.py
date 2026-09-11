from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import uuid

from app.models.domain import FinanceOperationsRecord
from app.repositories.domain import FinanceOperationsRepository
from app.schemas.domain import UnderwritingEvalRequest, UnderwritingEvalResponse

class FinanceOperationsService:
    def __init__(self, repo: FinanceOperationsRepository):
        self.repo = repo

    async def evaluate_underwriting(self, req: UnderwritingEvalRequest) -> UnderwritingEvalResponse:
        net_cash_flow = req.monthly_revenue - req.monthly_expenses
        estimated_pmt = req.requested_loan * 0.12
        dscr = round(net_cash_flow / max(estimated_pmt, 1.0), 2)
        is_approved = dscr >= 1.25 and net_cash_flow > 0
        status_str = "APPROVED" if is_approved else "HIGH_RISK_REJECTED"
        max_credit = round(net_cash_flow * 2.5, 2) if is_approved else round(max(net_cash_flow, 0) * 1.2, 2)

        record_id = f"FIN-{uuid.uuid4().hex[:8].upper()}"
        db_obj = FinanceOperationsRecord(
            id=record_id,
            enterprise_id=req.enterprise_id,
            monthly_revenue=req.monthly_revenue,
            monthly_expenses=req.monthly_expenses,
            dscr_ratio=dscr,
            underwriting_status=status_str
        )
        saved = await self.repo.create(db_obj)

        return UnderwritingEvalResponse(
            enterprise_id=saved.enterprise_id,
            monthly_net_cash_flow=net_cash_flow,
            dscr_ratio=saved.dscr_ratio,
            underwriting_status=saved.underwriting_status,
            max_credit_facility=max_credit,
            evaluated_at=saved.created_at
        )

    async def list_ledger(self, skip: int = 0, limit: int = 50) -> List[FinanceOperationsRecord]:
        return await self.repo.get_multi(skip=skip, limit=limit)
