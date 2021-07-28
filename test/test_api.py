import pytest

from app import app
from fastapi.testclient import TestClient
from typing import List


@pytest.fixture()
def user_selector() -> dict:
    return {"type": "By.xpath", "value": "//*[@value='Log In']"}


@pytest.fixture()
def user_selector_invalid_value() -> dict:
    return {"type": "By.xpath", "value": "hello, world!"}


@pytest.fixture()
def target_node() -> dict:
    return {
        "tag": "input",
        "classes": ["fadeIn", "fourth"],
        "other_attributes": {
            "_ngcontent-wvw-c3": "",
            "type": "button",
            "value": "Log In New",
        },
    }


@pytest.fixture()
def target_node_no_value() -> dict:
    return {
        "tag": "input",
        "classes": ["fadeIn", "fourth"],
        "other_attributes": {
            "_ngcontent-wvw-c3": "",
            "type": "button",
        },
    }


@pytest.fixture()
def expected_response() -> List[dict]:
    return [{"selector_type": "By.xpath", "selector_value": "//*[@value='Log In New']"}]


@pytest.fixture()
def expected_response_imitation_error() -> dict:
    return {
        "detail": [
            {
                "msg": "Unable to imitate the user selector: "
                "Target node does not have an attribute value."
            }
        ]
    }


@pytest.fixture()
def expected_response_parsing_error() -> dict:
    return {
        "detail": [
            {
                "msg": "Unable to parse the user selector: "
                "Cannot parse XPath selector."
            }
        ]
    }


def test_main():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200


def test_imitate(user_selector: dict, target_node: dict, expected_response: List[dict]):
    request_data = {"user_selector": user_selector, "target_node": target_node}
    with TestClient(app) as client:
        response = client.post("/imitate", json=request_data)
        assert response.status_code == 200
        assert response.json() == expected_response


def test_imitation_error(
    user_selector: dict,
    target_node_no_value: dict,
    expected_response_imitation_error: List[dict],
):
    request_data = {"user_selector": user_selector, "target_node": target_node_no_value}
    with TestClient(app) as client:
        response = client.post("/imitate", json=request_data)
        assert response.status_code == 422
        assert response.json() == expected_response_imitation_error


def test_parsing_error(
    user_selector_invalid_value: dict,
    target_node: dict,
    expected_response_parsing_error: List[dict],
):
    request_data = {
        "user_selector": user_selector_invalid_value,
        "target_node": target_node,
    }
    with TestClient(app) as client:
        response = client.post("/imitate", json=request_data)
        assert response.status_code == 422
        assert response.json() == expected_response_parsing_error
