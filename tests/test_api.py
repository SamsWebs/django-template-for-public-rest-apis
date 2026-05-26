from ninja.testing import TestClient

from app.api import api

client = TestClient(api)


def test_index_returns_success_status():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json()['status'] == 'Success'


def test_index_returns_about_message(settings):
    settings.ABOUT_MESSAGE = 'Hello from Django Ninja!'
    response = client.get('/')
    assert response.json()['result'] == 'Hello from Django Ninja!'
