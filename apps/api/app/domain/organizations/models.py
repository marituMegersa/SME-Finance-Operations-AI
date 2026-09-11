from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from app.db.base import Base

class SmeEnterprise(Base):
    __tablename__ = "sme_enterprises"

    id = Column(String, primary_key=True, index=True)
    enterprise_name = Column(String, nullable=False)
    registration_number = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    branches = relationship("FinancialBranch", back_populates="enterprise", cascade="all, delete-orphan")
