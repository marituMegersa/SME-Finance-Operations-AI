import pytest
from app.services.domain import FinanceOperationsService
from app.repositories.domain import FinanceOperationsRepository
from app.schemas.domain import UnderwritingEvalRequest

class MockSession:
    def add(self, obj): pass
    async def commit(self): pass
    async def refresh(self, obj): pass

@pytest.mark.asyncio
async def test_underwriting_approval_dscr():
    service = FinanceOperationsService(FinanceOperationsRepository(MockSession()))
    req = UnderwritingEvalRequest(
        enterprise_id="SME-ET-100",
        monthly_revenue=500000.0,
        monthly_expenses=300000.0,
        requested_loan=100000.0
    )
    res = await service.evaluate_underwriting(req)
    assert res.dscr_ratio >= 1.25
    assert res.underwriting_status == "APPROVED"
    assert res.monthly_net_cash_flow == 200000.0

@pytest.mark.asyncio
async def test_underwriting_high_risk_rejection():
    service = FinanceOperationsService(FinanceOperationsRepository(MockSession()))
    req = UnderwritingEvalRequest(
        enterprise_id="SME-ET-101",
        monthly_revenue=200000.0,
        monthly_expenses=250000.0,
        requested_loan=100000.0
    )
    res = await service.evaluate_underwriting(req)
    assert res.underwriting_status == "HIGH_RISK_REJECTED"
