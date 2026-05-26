from __future__ import annotations

from django.conf import settings
from django.http import HttpRequest
from ninja import NinjaAPI

api = NinjaAPI()


@api.get('/')
def index(request: HttpRequest) -> dict[str, str]:
    return {'status': 'Success', 'result': settings.ABOUT_MESSAGE}
