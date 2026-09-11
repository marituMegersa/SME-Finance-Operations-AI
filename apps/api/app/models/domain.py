from sqlalchemy import Column, String, DateTime, Float, JSON
import datetime
from app.core.database import Base

class FinanceOperationsRecord(Base):
    __tablename__ = "finance_operations_records"
    id = Column(String, primary_key=True, index=True)
    enterprise_id = Column(String, nullable=False, index=True)
    monthly_revenue = Column(Float, nullable=False)
    monthly_expenses = Column(Float, nullable=False)
    dscr_ratio = Column(Float, default=1.0)
    underwriting_status = Column(String, default="PENDING")
    created_at = Column(DateTime, default=datetime.datetime.utcnow, index=True)
