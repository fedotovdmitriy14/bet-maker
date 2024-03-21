def test_make_new_bet(client, set_up_and_tear_down_bets):
    response = client.post(
        f'api/v1/bets',
        json={
            "event_id": 1511,
            "bet_sum": 1511
        }
    )
    assert response.status_code == 201


def test_get_all_bets(client, set_up_and_tear_down_bets):
    response = client.get(
        f'api/v1/bets',
    )
    assert response.status_code == 200
    assert len(response.json()) == 5


def test_get_all_bets_pagination(client, set_up_and_tear_down_bets):
    response = client.get(
        f'api/v1/bets',
        params={
            'page_size': 2
        }
    )
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_put_new_status_to_event(client, set_up_and_tear_down_bets):
    response = client.put(
        f'api/v1/events/{1111}',
        params={
            'status': 'WIN'
        }
    )
    assert response.status_code == 200
