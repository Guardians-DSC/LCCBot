from unittest import mock

import pytest

from api import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


@pytest.fixture
def schedule_valido():
    LCC1 = []
    LCC2 = [
        { "course" : "Lab. de Prog2", "startTime": "10:00", "endTime": "12:00" },
        { "course" : "Prog1", "startTime": "08:00", "endTime": "10:00" }
    ]
    LCC3 = []
    return {"LCC1": LCC1, "LCC2": LCC2, "LCC3": LCC3}


@mock.patch('src.services.scheduleService.scheduleService')
def test_schedule_service_valido(mock_schedule_service, schedule_valido, client):
    mock_schedule_service.return_value = expected_schedule = schedule_valido
    expected_status_code = 200

    response = client.get('/schedule')
    actual_schedule = response.json
    actual_status_code = response.status_code

    assert actual_status_code == expected_status_code
    assert all(actual_schedule[campo] == expected_schedule[campo] for campo in expected_schedule)
    assert all(campo in expected_schedule for campo in actual_schedule)