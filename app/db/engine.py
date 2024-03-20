from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.constants import settings

engine = create_async_engine(f"postgresql+asyncpg://{settings.db_user}:{settings.db_password}@{settings.db_host}:"
                             f"{settings.db_port}/{settings.db_name}")  # noqa: P101
Session = sessionmaker(bind=engine, class_=AsyncSession)


async def get_db(request: Request) -> AsyncSession:
    async with Session() as session:
        yield session
