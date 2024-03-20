from fastapi import FastAPI
from starlette.responses import JSONResponse

from app.api.v1 import bets, events
from app.services.helpers import CustomException


app = FastAPI(
    title='Bet maker API',
    version='1.0.0',
)
app.include_router(bets.router, prefix='/api/v1/bets', tags=['bets'])
app.include_router(events.router, prefix='/api/v1/events', tags=['events'])


@app.get('/')
async def status():
    return {'status': 'OK'}


@app.exception_handler(CustomException)
async def custom_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.code,
        content={"message": exc.message, "code": exc.code}
    )
