from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from app.models.domain import FinanceOperationsRecord

class FinanceOperationsRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_id(self, record_id: str) -> Optional[FinanceOperationsRecord]:
        result = await self.db.execute(select(FinanceOperationsRecord).where(FinanceOperationsRecord.id == record_id))
        return result.scalars().first()

    async def get_multi(self, skip: int = 0, limit: int = 50) -> List[FinanceOperationsRecord]:
        result = await self.db.execute(select(FinanceOperationsRecord).offset(skip).limit(limit))
        return result.scalars().all()

    async def create(self, record: FinanceOperationsRecord) -> FinanceOperationsRecord:
        self.db.add(record)
        await self.db.commit()
        await self.db.refresh(record)
        return record
