from fastapi import APIRouter, status
from pydantic import BaseModel
from app.domain.finance_operations.service import FinanceOperationsService

router = APIRouter(prefix="/api/v1/finance_operations", tags=["Finance Operations"])

class LoanInput(BaseModel):
    sme_account_id: str
    monthly_revenue: float
    monthly_expense: float
    outstanding_invoices_amount: float

@router.post("/underwrite", status_code=status.HTTP_200_OK)
def underwrite_loan(data: LoanInput):
    return FinanceOperationsService.underwrite_loan(data.sme_account_id, data.monthly_revenue, data.monthly_expense, data.outstanding_invoices_amount)
