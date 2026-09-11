from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class CreditOfficer(Base):
    __tablename__ = "credit_officers"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    officer_code = Column(String, nullable=False)
    branch_id = Column(String, ForeignKey("financial_branches.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    branch = relationship("FinancialBranch", back_populates="credit_officers")
