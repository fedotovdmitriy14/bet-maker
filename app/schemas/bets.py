from datetime import datetime
from enum import Enum

from pydantic import BaseModel
from uuid import UUID

from app.db.models.bets import Statuses


class BetPost(BaseModel):
    bet_sum: float
    event_id: int


class BetId(BaseModel):
    id: UUID

    class Config:
        orm_mode = True


class Bet(BetId, BetPost):
    created_at: datetime
    bet_sum: float
    status: Statuses


class ResultStatus(str, Enum):
    WIN = "WIN"
    LOSE = "LOSE"
