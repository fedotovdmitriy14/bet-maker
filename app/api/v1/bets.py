from fastapi import APIRouter, Depends

from app.db.models.bets import Bets
from app.schemas.bets import BetPost, BetId
from app.services.async_search_service import AsyncSearchService, get_search_service

router = APIRouter()


@router.post(
    '/',
    response_model=BetId,
)
async def post_new_bet(
    payload: BetPost,
    base_service: AsyncSearchService = Depends(get_search_service)
) -> BetId:
    return await base_service.save(data=payload, model=Bets)
