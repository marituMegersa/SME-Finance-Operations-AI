from sqlalchemy.orm import Session
from typing import List
import uuid
from app.domain.finance_operations.models import FinanceOperationsRecord
from app.domain.finance_operations.schemas import UnderwritingEvalRequest, UnderwritingEvalResponse
from app.domain.finance_operations.engine import CreditUnderwritingEngine

class FinanceOperationsService:
    @staticmethod
    def underwrite_and_store(db: Session, req: UnderwritingEvalRequest) -> UnderwritingEvalResponse:
        res = CreditUnderwritingEngine.evaluate_credit(
            monthly_revenue=req.monthly_revenue,
            monthly_expenses=req.monthly_expenses,
            requested_loan=req.requested_loan
        )
        
        record_id = f"FIN-{uuid.uuid4().hex[:8].upper()}"
        db_obj = FinanceOperationsRecord(
            id=record_id,
            enterprise_id=req.enterprise_id,
            monthly_revenue=req.monthly_revenue,
            monthly_expenses=req.monthly_expenses,
            dscr_ratio=res["dscr_ratio"],
            underwriting_status=res["underwriting_status"]
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        
        return UnderwritingEvalResponse(
            enterprise_id=db_obj.enterprise_id,
            monthly_net_cash_flow=res["net_cash_flow"],
            dscr_ratio=db_obj.dscr_ratio,
            underwriting_status=db_obj.underwriting_status,
            max_credit_facility=res["max_credit_facility"],
            evaluated_at=db_obj.created_at
        )

    @staticmethod
    def list_records(db: Session, skip: int = 0, limit: int = 50) -> List[FinanceOperationsRecord]:
        return db.query(FinanceOperationsRecord).offset(skip).limit(limit).all()
