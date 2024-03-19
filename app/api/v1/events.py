from typing import Dict

from fastapi import APIRouter, Depends, Path

from app.schemas.bets import ResultStatus
from app.services.async_search_service import AsyncSearchService, get_search_service

router = APIRouter()


@router.put(
    '/{id}',
)
async def update_bets_with_event_id(
    status: ResultStatus,
    id_: int = Path(alias='id'),
    base_service: AsyncSearchService = Depends(get_search_service)
) -> Dict[str, str]:
    await base_service.update_bets_status(status=status, event_id=id_)
    return {'message': 'ok'}
