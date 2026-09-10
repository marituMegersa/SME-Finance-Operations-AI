from typing import Dict, Any
import uuid

class FinanceOperationsService:
    @staticmethod
    def underwrite_loan(sme_account_id: str, monthly_revenue: float, monthly_expense: float, outstanding_invoices: float) -> Dict[str, Any]:
        net_cash_flow = monthly_revenue - monthly_expense
        debt_coverage_ratio = (net_cash_flow + outstanding_invoices * 0.7) / (monthly_expense + 1.0)
        
        credit_score = min(0.99, max(0.40, debt_coverage_ratio * 0.5))
        decision = "APPROVED" if credit_score >= 0.75 else "CONDITIONAL_APPROVAL"
        
        return {
            "assessment_id": f"UW-{uuid.uuid4().hex[:8]}",
            "sme_account_id": sme_account_id,
            "net_monthly_cash_flow": net_cash_flow,
            "credit_score": round(credit_score, 2),
            "underwriting_decision": decision,
            "max_eligible_micro_loan": round(net_cash_flow * 3.5, 2)
        }
