from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.domain import UnderwritingEvalResponse

class FinanceSearchQuery(BaseModel):
    min_dscr: Optional[float] = Field(None, example=1.25)
    status: Optional[str] = Field(None, example="APPROVED")
    page: int = Field(1, ge=1)
    page_size: int = Field(20, ge=1, le=100)

class PaginatedFinanceResponse(BaseModel):
    items: List[UnderwritingEvalResponse]
    total: int
    page: int
    page_size: int
    total_pages: int
