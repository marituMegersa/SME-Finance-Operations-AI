from pydantic import BaseModel, Field
from typing import Dict, List

class FinanceAnalyticsResponse(BaseModel):
    total_underwritings: int = Field(..., example=320)
    approved_loans_count: int = Field(..., example=215)
    rejected_high_risk_count: int = Field(..., example=105)
    average_dscr_ratio: float = Field(..., example=1.45)
    total_credit_granted_etb: float = Field(..., example=45000000.0)
