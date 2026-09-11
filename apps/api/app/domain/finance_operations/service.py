from app.domain.finance_operations.engine import CreditUnderwritingEngine
from app.domain.finance_operations.schemas import UnderwritingEvalRequest, UnderwritingEvalResponse

class FinanceOperationsService:
    @staticmethod
    def evaluate_underwriting(req: UnderwritingEvalRequest) -> UnderwritingEvalResponse:
        res = CreditUnderwritingEngine.evaluate_credit(
            monthly_revenue=req.monthly_revenue,
            monthly_expenses=req.monthly_expenses,
            requested_loan=req.requested_loan
        )
        return UnderwritingEvalResponse(
            enterprise_id=req.enterprise_id,
            monthly_net_cash_flow=res["net_cash_flow"],
            dscr_ratio=res["dscr_ratio"],
            underwriting_status=res["underwriting_status"],
            max_credit_facility=res["max_credit_facility"]
        )
