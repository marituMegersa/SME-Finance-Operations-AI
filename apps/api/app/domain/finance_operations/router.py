from fastapi import APIRouter
from app.domain.finance_operations.service import *

router = APIRouter(prefix="/api/v1/finance_operations", tags=["SME Finance & Cash Flow Operations"])

@router.get("/status")
def get_domain_status():
    return {"status": "active", "domain": "SME Finance & Cash Flow Operations"}
