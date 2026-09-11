from typing import Dict, Any

class CreditUnderwritingEngine:
    @staticmethod
    def evaluate_credit(monthly_revenue: float, monthly_expenses: float, requested_loan: float) -> Dict[str, Any]:
        net_cash_flow = monthly_revenue - monthly_expenses
        estimated_monthly_payment = requested_loan * 0.12
        dscr = round(net_cash_flow / max(estimated_monthly_payment, 1.0), 2)
        
        is_approved = dscr >= 1.25 and net_cash_flow > 0
        max_loan_facility = round(net_cash_flow * 2.5, 2) if is_approved else round(max(net_cash_flow, 0) * 1.2, 2)
        
        return {
            "net_cash_flow": net_cash_flow,
            "dscr_ratio": dscr,
            "underwriting_status": "APPROVED" if is_approved else "HIGH_RISK_REJECTED",
            "max_credit_facility": max_loan_facility
        }
