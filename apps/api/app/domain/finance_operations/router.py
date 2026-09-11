from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.finance_operations.schemas import UnderwritingEvalRequest, UnderwritingEvalResponse
from app.domain.finance_operations.service import FinanceOperationsService

router = APIRouter(prefix="/api/v1/finance_operations", tags=["Credit Underwriting & Cash Flow"])

@router.post("/underwrite", response_model=UnderwritingEvalResponse, status_code=status.HTTP_201_CREATED)
def evaluate_underwriting(req: UnderwritingEvalRequest, db: Session = Depends(get_db)):
    return FinanceOperationsService.underwrite_and_store(db, req)

@router.get("/ledger")
def list_finance_records(skip: int = Query(0, ge=0), limit: int = Query(50, le=100), db: Session = Depends(get_db)):
    return FinanceOperationsService.list_records(db, skip=skip, limit=limit)
