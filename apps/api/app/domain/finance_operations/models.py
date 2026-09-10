from sqlalchemy import Column, String, Boolean, DateTime, Float, Integer, JSON
import datetime
from app.db.base import Base

class FinanceOperationsRecord(Base):
    __tablename__ = "finance_operations_records"

    id = Column(String, primary_key=True, index=True)

    sme_account_id = Column(String, nullable=False, index=True)
    monthly_revenue = Column(Float, nullable=False)
    monthly_expense = Column(Float, nullable=False)
    credit_risk_score = Column(Float, default=0.85)
    cash_flow_forecast = Column(JSON, nullable=False)
    loan_approval_recommendation = Column(String, default="APPROVED")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
