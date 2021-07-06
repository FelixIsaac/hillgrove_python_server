
from os import getenv
from json import loads as load_json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Session


@csrf_exempt
def get_sessions(request, session=None):
    if session:
        session_object = Session.objects.values().get(id=session)

        return JsonResponse({
            'error': False,
            'session': session_object
        })
    else:
        sessions = Session.objects.all().values()

        return JsonResponse({
            'error': False,
            'sessions': list(sessions)
        })
