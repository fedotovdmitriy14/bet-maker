from typing import Dict

from fastapi import APIRouter, Depends

from app.db.models.bets import Bets
from app.schemas.bets import BetPost
from app.services.async_search_service import AsyncSearchService, get_search_service

router = APIRouter()


@router.post(
    '/',
)
async def post_new_bet(
    payload: BetPost,
    base_service: AsyncSearchService = Depends(get_search_service)
) -> Dict[str, str]:
    await base_service.save(data=payload, model=Bets)
    return {'message': 'ok'}
