from datetime import datetime

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
