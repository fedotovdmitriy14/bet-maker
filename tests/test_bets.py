def test_make_new_bet(client):
    response = client.post(
        f'api/v1/bets',
        json={
            "event_id": 1511,
            "bet_sum": 1511
        }
    )
    assert response.status_code == 201
