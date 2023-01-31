import os
import datetime

import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def api_test_client(data_file):
    client = TestClient(app)
    return client


@pytest.fixture
def data_file_content():
    return "REFACTORING SERVICE\n"


SATURDAY = datetime.datetime(2023, 1, 28, 11, 11, 11)
MONDAY = datetime.datetime(2023, 1, 30, 11, 11, 11)
TUESDAY = datetime.datetime(2023, 1, 31, 11, 11, 11)


def get_day_name(val):
    if isinstance(val, (datetime.datetime,)):
        # note this wouldn't show any hours/minutes/seconds
        return val.strftime("%A")


@pytest.fixture
def patch_datetime_now(monkeypatch, request):
    class MyDateTime:
        @classmethod
        def now(cls):
            return request.param

    monkeypatch.setattr(datetime, "datetime", MyDateTime)


@pytest.fixture
def data_file(mocker, data_file_content):
    read_mock = mocker.mock_open(read_data=data_file_content)
    m = mocker.patch("builtins.open", read_mock)
    return m


def test_get_service_name(api_test_client, data_file, data_file_content):
    response = api_test_client.get("/get-service-name")
    assert response.status_code == 200
    assert response.json() == {"result": data_file_content}


@pytest.mark.parametrize(
    "patch_datetime_now", [MONDAY, TUESDAY, SATURDAY], ids=get_day_name
)
def test_magic_day(api_test_client, patch_datetime_now):
    response = api_test_client.get("/magic-day")
    assert response.status_code == 200
    if datetime.datetime.now().weekday() % 2 == 0:
        assert response.json() == {"result": True}
    else:
        assert response.json() == {"result": False}


@pytest.mark.parametrize(
    "patch_datetime_now", [MONDAY, TUESDAY, SATURDAY], ids=get_day_name
)
def test_is_weekends(api_test_client, patch_datetime_now):
    response = api_test_client.get("/is-weekends")
    assert response.status_code == 200
    if datetime.datetime.now().weekday() < 5:
        assert response.json() == {"result": False}
    else:
        assert response.json() == {"result": True}


def test_is_valid_user(api_test_client):
    user = "Ahmed"
    age = 30
    job = "data scientist"
    response = api_test_client.get(f"/is-valid-user?user={user}&age={age}&job={job}")
    assert response.status_code == 200
    assert response.json() == {"result": True}

    user = "Ahmed"
    age = 30
    job = "data engineer"
    response = api_test_client.get(f"/is-valid-user?user={user}&age={age}&job={job}")
    assert response.status_code == 200
    assert response.json() == {"result": False}


def test_capitalize_string(api_test_client):
    test_string = "some test string"
    response = api_test_client.post(f"/capitalize-string?s={test_string}")
    assert response.status_code == 200
    assert response.json() == {"result": test_string.upper()}


def test_capitalize_list(api_test_client):
    test_list_string = "some,test,list"

    test_list = test_list_string.split(",")
    expected_result = list(map(str.upper, test_list))

    response = api_test_client.post(f"/capitalize-list?s={test_list_string}")
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


def test_send_email(api_test_client):
    provider = "mailgun"
    message = "some email"
    response = api_test_client.post(f"/send-email?provider={provider}&m={message}")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_get_user(api_test_client):
    username = "John"
    response = api_test_client.get(f"/get-user-id?username={username}")
    assert response.status_code == 200
    assert response.json() == {"user_id": 12}


def test_get_user_id_not_found(api_test_client):
    username = "Paul"
    response = api_test_client.get(f"/get-user-id?username={username}")
    assert response.status_code == 404
    assert response.json() == {"message": "User not found"}


def test_get_items(api_test_client):
    response = api_test_client.get("/items")
    assert response.status_code == 200
    assert response.json() == {
        "response": [
            {"title": "1 item", "is_published": True},
            {"title": "4 item", "is_published": True},
        ]
    }


def test_get_key(api_test_client):
    key_id = 1
    response = api_test_client.get(f"/key/{key_id}")
    assert response.status_code == 200
    assert response.json() == {"result": "key1"}


def test_number_in_both_lists(api_test_client):
    key_id = 1
    response = api_test_client.get(f"/number-in-both-lists/{key_id}")
    assert response.status_code == 200
    assert response.json() == {"result": False}

    key_id = 3
    response = api_test_client.get(f"/number-in-both-lists/{key_id}")
    assert response.status_code == 200
    assert response.json() == {"result": True}


def test_add_id(api_test_client):
    new_id = 1
    response = api_test_client.post(f"/add-id?new_id={new_id}")
    assert response.status_code == 200
    assert response.json() == {"result": [new_id]}

    another_id = 2
    response = api_test_client.post(f"/add-id?new_id={another_id}")
    assert response.status_code == 200
    assert response.json() == {"result": [new_id, another_id]}


def test_round_to_ceil(api_test_client):
    number = 3.5
    expected_result = 4
    response = api_test_client.get(f"/round?number={number}")
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


def test_round_to_floor(api_test_client):
    number = 3.5
    expected_result = 3
    response = api_test_client.get(f"/round?number={number}&to_ceil=false")
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


def test_multiply(api_test_client):
    first_number = 3
    second_number = 4
    expected_result = first_number * second_number
    response = api_test_client.post(
        f"/multiply?first_number={first_number}&second_number={second_number}"
    )
    assert response.status_code == 200
    assert response.json() == {"result": expected_result}


def test_multiply_security(api_test_client):
    malicious_code_first_number = (
        "exec('import os; result = os.system(\"touch hack.txt\")')#"
    )
    second_number = 4
    try:
        response = api_test_client.post(
            f"/multiply?first_number={malicious_code_first_number}&second_number={second_number}"
        )
    except Exception as exception:
        print("Expected exception", exception)
    assert (
        os.path.exists("hack.txt") == False
    ), "Security breach! Malicious code executed via API - hack.txt was created!"
