from pydantic import BaseModel
from uuid import UUID


class BetPost(BaseModel):
    bet_sum: float


class BetId(BaseModel):
    id: UUID

    class Config:
        orm_mode = True
