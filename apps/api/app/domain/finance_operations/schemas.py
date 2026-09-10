from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class FinanceOperationsRequest(BaseModel):

    sme_account_id: str
    monthly_revenue: float
    monthly_expense: float
    outstanding_invoices_amount: float


class FinanceOperationsResponse(BaseModel):
    id: str
    status: str = "COMPLETED"
    summary: str
    confidence_score: float = 0.98
    created_at: datetime

    class Config:
        from_attributes = True
