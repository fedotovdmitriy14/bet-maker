import logging
from datetime import datetime

from functools import lru_cache
from typing import Type

from fastapi import Depends
from sqlalchemy import exc, select
from sqlalchemy.orm import DeclarativeMeta

from app.db.engine import Session, get_db
from app.services import AsyncSearchEngine
from app.services.helpers import CustomException


logger = logging.getLogger(__name__)


class AsyncSearchService(AsyncSearchEngine):
    """Класс для запросов в базу."""
    def __init__(self, db: Session) -> None:
        self.db = db

    async def save(self, data, model: Type[DeclarativeMeta]):
        """Сохранить новую запись."""

        item = model(**data.dict() | {'created_at': datetime.now()})
        self.db.add(item)
        try:
            await self.db.commit()
        except exc.IntegrityError:
            raise CustomException(
                code=409,
                message=f'Could not save',
            )
        await self.db.refresh(item)
        return item

    async def update(self):
        """Обновить запись."""
        pass

    async def get_all(self, model: Type[DeclarativeMeta], page_size: int, page: int):
        """Получить все записи из бд."""
        query = select(model).limit(page_size).offset((page - 1) * page_size)
        # if getattr(model, 'created_at'):
        #     query = select(model).order_by(model.created_at).limit(page_size).offset((page - 1) * page_size)
        result = await self.db.execute(query)
        bets = result.scalars().all()
        return bets


@lru_cache()
def get_search_service(
    db: Session = Depends(get_db),
) -> AsyncSearchService:
    return AsyncSearchService(db=db)
