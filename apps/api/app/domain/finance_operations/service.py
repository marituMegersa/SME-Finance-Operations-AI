from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.finance_operations.models import FinanceOperationsRecord
from app.domain.finance_operations.schemas import FinanceOperationsRequest

class FinanceOperationsService:
    @staticmethod
    def process_encounter(db: Session, data: FinanceOperationsRequest) -> FinanceOperationsRecord:
        rec_id = f"REC-{uuid.uuid4().hex[:8]}"
        db_obj = FinanceOperationsRecord(
            id=rec_id,
            created_at=datetime.datetime.utcnow()
        )
        return db_obj
