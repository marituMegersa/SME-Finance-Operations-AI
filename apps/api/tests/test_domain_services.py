def test_finance_operations_model_instantiation():
    from app.domain.finance_operations.models import FinanceOperationsRecord
    rec = FinanceOperationsRecord(id="REC-TEST-01")
    assert rec.id == "REC-TEST-01"

def test_finance_operations_schema_validation():
    from app.domain.finance_operations.schemas import FinanceOperationsResponse
    res = FinanceOperationsResponse(id="REC-TEST-01", status="COMPLETED", summary="Test", confidence_score=0.99, created_at="2026-09-10T16:00:00Z")
    assert res.status == "COMPLETED"
