import asyncio

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.constants import settings
from app.db.engine import get_db
from app.main import app
from tests.fake_db import tear_down_bets_fixture, set_up_bets_fixture


@pytest.fixture(scope='session')
def async_session():
    engine = create_async_engine(
        f"postgresql+asyncpg://{settings.db_user}:{settings.db_password}@{settings.db_host}:"
        f"{settings.db_port}/{settings.db_name}",
        poolclass=NullPool,
    )
    async_session = sessionmaker(bind=engine, class_=AsyncSession)
    yield async_session
    engine.sync_engine.dispose()


@pytest.fixture
def client(async_session):
    async def override_get_db():
        try:
            db = async_session()
            yield db
        finally:
            await db.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture(scope='session')
def loop():
    event_loop = asyncio.new_event_loop()
    yield event_loop
    event_loop.close()


@pytest.fixture
def set_up_and_tear_down_bets(async_session, loop):
    created_tables = loop.run_until_complete(set_up_bets_fixture(async_session))
    yield created_tables
    loop.run_until_complete(tear_down_bets_fixture(async_session))
