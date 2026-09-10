from sqlalchemy import Column, String, DateTime
import datetime
from app.db.base import Base

class FinancialBranch(Base):
    __tablename__ = "financial_branches"

    id = Column(String, primary_key=True, index=True)
    branch_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
