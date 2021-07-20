
from os import getenv
from json import loads as load_json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from jwt import encode as encode_jwt, decode as decode_jwt
from authentication.models import User
from users.models import SolutionProgress
from .models import Session, Topic, Solution


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


@csrf_exempt
def get_solution(request, topic, solution):
    if not topic or not solution:
        return JsonResponse({
            'error': True,
            'message': 'Topic and solution parameters need'
        })

     # authorization and authentication
    if 'Authorization' not in request.headers:
        return JsonResponse({
            'error': True,
            'message': 'Missing authorization header'
        }, status=401)

    user_token = request.headers.get('Authorization')

    try:
        payload = decode_jwt(user_token, getenv(
            'JWT_SECRET'), algorithms='HS256')
    except Exception as error:
        return JsonResponse({
            'error': True,
            'message': 'Invalid JWT token'
        }, status=401)

    user = User.objects.get(google_id=payload['googleId'])

    if not user:
        return JsonResponse({
            'error': True,
            'message': 'User not found'
        }, status=404)

    # actual route code
    if request.method == 'GET':
        pass
    else:
        return JsonResponse({
            'error': True,
            'message': 'Server does not know how to handle your method'
        }, status=400)

    try:
        solution = Solution.objects.filter(name=solution, topic=topic)
    except:
        return JsonResponse({
            'error': True,
            'message': 'Solution not found'
        })

    if not len(solution):
        return JsonResponse({
            'error': True,
            'message': 'Solution not found'
        })

    # solution found
    SolutionProgress.objects.update_or_create(
        user=user,
        solution_id=solution[0].id,
        defaults={
            'shown_solution': True
        }
    )

    return JsonResponse({
        'error': False,
        'solution': solution[0].solution
    })


@csrf_exempt
def get_hint(request, topic, solution):
    if not topic or not solution:
        return JsonResponse({
            'error': True,
            'message': 'Topic and solution parameters need'
        })

     # authorization and authentication
    if 'Authorization' not in request.headers:
        return JsonResponse({
            'error': True,
            'message': 'Missing authorization header'
        }, status=401)

    user_token = request.headers.get('Authorization')

    try:
        payload = decode_jwt(user_token, getenv(
            'JWT_SECRET'), algorithms='HS256')
    except Exception as error:
        return JsonResponse({
            'error': True,
            'message': 'Invalid JWT token'
        }, status=401)

    user = User.objects.get(google_id=payload['googleId'])

    if not user:
        return JsonResponse({
            'error': True,
            'message': 'User not found'
        }, status=404)

    # actual route code
    if request.method == 'GET':
        SolutionProgress.objects.update_or_create(
            solution_id=solution,
            user=user,
            defaults={
                'shown_hint': True
            }
        )
    else:
        return JsonResponse({
            'error': True,
            'message': 'Server does not know not know how to handle your method'
        })
