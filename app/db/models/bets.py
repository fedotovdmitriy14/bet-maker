import uuid

from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Bets(Base):
    __tablename__ = 'bets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_id = Column(Integer)
    bet_sum = Column(Float)
    status = Column(String)
    created_at = Column(DateTime)
