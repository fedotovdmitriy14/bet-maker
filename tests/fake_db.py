from datetime import datetime

from sqlalchemy import delete

from app.db.models.bets import Bets, Statuses


async def set_up_bets_fixture(session):
    async with session() as session:
        async with session.begin():
            session.add_all(
                [
                    Bets(
                        event_id=1111,
                        bet_sum=100,
                        status=Statuses.not_played,
                        created_at=datetime(2023, 7, 4, 18, 00, 00),
                    ),
                    Bets(
                        event_id=1111,
                        bet_sum=200,
                        status=Statuses.not_played,
                        created_at=datetime(2023, 4, 4, 18, 00, 00),
                    ),
                    Bets(
                        event_id=1111,
                        bet_sum=1000,
                        status=Statuses.not_played,
                        created_at=datetime(2023, 9, 4, 18, 00, 00),
                    ),
                    Bets(
                        event_id=1112,
                        bet_sum=200,
                        status=Statuses.not_played,
                        created_at=datetime(2023, 10, 4, 18, 00, 00),
                    ),
                    Bets(
                        event_id=1112,
                        bet_sum=1000,
                        status=Statuses.not_played,
                        created_at=datetime(2023, 8, 4, 18, 00, 00),
                    ),
                ]
            )


async def tear_down_bets_fixture(session):
    async with session() as session:
        async with session.begin():
            await session.execute(delete(Bets))
