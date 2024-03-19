import uuid
import enum

from sqlalchemy import Column, DateTime, Integer, Float
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Statuses(enum.Enum):
    not_played = "not_played"
    win = "win"
    lose = "lose"


class Bets(Base):
    __tablename__ = 'bets'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    event_id = Column(Integer)
    bet_sum = Column(Float)
    status = Column(ENUM(Statuses), default=Statuses.not_played)
    created_at = Column(DateTime)
