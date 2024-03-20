def test_make_new_bet(client):
    response = client.post(
        f'api/v1/bets',
        json={
            "event_id": 1511,
            "bet_sum": 1511
        }
    )
    assert response.status_code == 201


def test_get_all_bets(client, set_up_and_tear_down_bets):
    response = client.post(
        f'api/v1/bets',
    )
    assert response.status_code == 200
    assert len(response.json()) == 5
