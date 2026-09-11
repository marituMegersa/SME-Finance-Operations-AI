from fastapi import APIRouter
from app.domain.finance_operations.schemas import UnderwritingEvalRequest, UnderwritingEvalResponse
from app.domain.finance_operations.service import FinanceOperationsService

router = APIRouter(prefix="/api/v1/finance_operations", tags=["Credit Underwriting & Cash Flow"])

@router.post("/underwrite", response_model=UnderwritingEvalResponse)
def evaluate_underwriting(req: UnderwritingEvalRequest):
    return FinanceOperationsService.evaluate_underwriting(req)
