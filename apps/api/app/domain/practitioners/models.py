from sqlalchemy import Column, String, DateTime
import datetime
from app.db.base import Base

class CreditOfficer(Base):
    __tablename__ = "credit_officers"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    officer_code = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
