from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class FinancialBranch(Base):
    __tablename__ = "financial_branches"

    id = Column(String, primary_key=True, index=True)
    branch_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    enterprise_id = Column(String, ForeignKey("sme_enterprises.id"), nullable=True, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    enterprise = relationship("SmeEnterprise", back_populates="branches")
    credit_officers = relationship("CreditOfficer", back_populates="branch", cascade="all, delete-orphan")
