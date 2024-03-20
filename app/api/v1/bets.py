from typing import List

from fastapi import APIRouter, Depends, Query

from app.db.models.bets import Bets
from app.schemas.bets import BetPost, BetId, Bet
from app.services.async_search_service import AsyncSearchService, get_search_service

router = APIRouter()


@router.post(
    '/',
    status_code=201,
    response_model=BetId,
)
async def post_new_bet(
    payload: BetPost,
    base_service: AsyncSearchService = Depends(get_search_service)
) -> BetId:
    return await base_service.save(data=payload, model=Bets)


@router.get(
    '/',
    response_model=List[Bet],
)
async def get_all_bets(
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1),
    base_service: AsyncSearchService = Depends(get_search_service)
) -> List[Bet]:
    return await base_service.get_all(model=Bets, page=page, page_size=page_size)
