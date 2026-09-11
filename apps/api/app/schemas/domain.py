from pydantic import BaseModel, Field
from datetime import datetime

class UnderwritingEvalRequest(BaseModel):
    enterprise_id: str = Field(..., example="SME-ET-9921")
    monthly_revenue: float = Field(..., ge=0, example=450000.0)
    monthly_expenses: float = Field(..., ge=0, example=280000.0)
    requested_loan: float = Field(..., ge=0, example=100000.0)

class UnderwritingEvalResponse(BaseModel):
    enterprise_id: str
    monthly_net_cash_flow: float
    dscr_ratio: float
    underwriting_status: str
    max_credit_facility: float
    evaluated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
