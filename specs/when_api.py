from ninja.testing import TestClient

from app.api import api

client = TestClient(api)


class DescribeIndex:
    def should_return_success_status(self) -> None:
        response = client.get('/')
        assert response.status_code == 200
        assert response.json()['status'] == 'Success'

    def should_return_about_message(self, settings) -> None:
        settings.ABOUT_MESSAGE = 'Hello from Django Ninja!'
        response = client.get('/')
        assert response.json()['result'] == 'Hello from Django Ninja!'
