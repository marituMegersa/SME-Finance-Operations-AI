from typing import Dict, Any
import uuid

class FinanceOperationsService:
    @staticmethod
    def underwrite_loan(sme_account_id: str, monthly_revenue: float, monthly_expense: float, invoices: float) -> Dict[str, Any]:
        net_cash_flow = monthly_revenue - monthly_expense
        score = min(0.99, max(0.40, (net_cash_flow + invoices * 0.7) / (monthly_expense + 1.0) * 0.5))
        return {
            "assessment_id": f"UW-{uuid.uuid4().hex[:8]}",
            "sme_account_id": sme_account_id,
            "credit_score": round(score, 2),
            "underwriting_decision": "APPROVED" if score >= 0.75 else "CONDITIONAL",
            "eligible_loan_amount": round(net_cash_flow * 3.5, 2)
        }
