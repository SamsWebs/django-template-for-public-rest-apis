from django.conf import settings
from ninja import NinjaAPI

api = NinjaAPI()


@api.get('/')
def index(request):
    return {'status': 'Success', 'result': settings.ABOUT_MESSAGE}
