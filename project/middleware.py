from django.conf import settings
from django.utils import translation
from .models import *
from django.contrib.auth.models import Group

class ForceLangMiddleware:
    def process_request(self, request):
        request.LANG = getattr(settings, 'LANGUAGE_CODE', settings.LANGUAGE_CODE)
        translation.activate(request.LANG)
        request.LANGUAGE_CODE = request.LANG
