from pydantic import BaseModel


class BetPost(BaseModel):
    bet_sum: float
