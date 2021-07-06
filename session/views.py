
from os import getenv
from json import loads as load_json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Session, Topic


@csrf_exempt
def get_sessions(request, session=None):
    if session:
        session_object = Session.objects.values().get(id=session)
        topics = Topic.objects.values().filter(session=session_object['id'])

        return JsonResponse({
            'error': False,
            'session': {
                **session_object,
                'topics': list(topics)
            }
        })
    else:
        sessions = Session.objects.all().values()

        return JsonResponse({
            'error': False,
            'sessions': [
                {
                    **session,
                    'topics': list(Topic.objects.values().filter(session=session['id']))
                } for session in sessions
            ]
        })
