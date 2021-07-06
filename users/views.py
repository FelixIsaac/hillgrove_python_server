from os import getenv
from json import loads as load_json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from jwt import encode as encode_jwt, decode as decode_jwt
from authentication.models import User
from session.models import Session, Topic
from .models import Progress


@csrf_exempt
def progress(request, session=None):
    if request.method not in ['GET', 'PATCH']:
        return JsonResponse({
            'error': True,
            'message': 'Server does not know how to handle your method'
        }, status=400)

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
        if session:
            try:
                progress = Progress.objects.filter(
                    user=user,
                    last_session__id=session
                )
            except:
                return JsonResponse({
                    'error': True,
                    'message': 'Progress not found'
                })

            if not len(progress):
                return JsonResponse({
                    'error': True,
                    'message': 'Progress not found'
                })

            return JsonResponse({
                'error': False,
                'last_session': progress[0].last_session.name,
                'last_topic': progress[0].last_session.name
            })
        else:
            try:
                progress = Progress.objects.filter(user=user)
            except:
                return JsonResponse({
                    'error': True,
                    'message': 'Progress not found'
                })

            def mapProgress(progress_item):
                return {
                    'last_session': progress_item.last_session.name,
                    'last_topic': progress_item.last_session.name
                }

            return JsonResponse({
                'error': False,
                'sessions': list(map(mapProgress, progress))
            })
    elif request.method == 'PATCH':
        body = load_json(request.body)

        try:
            session = Session.objects.get(name=body['last_session'])
            topic = Topic.objects.get(name=body['last_topic'])
        except:
            return JsonResponse({
                'error': True,
                'message': 'Invalid session or topic'
            })

        # create progress row if there is no progress row in progress table
        if not Progress.objects.filter(user=user, last_session=session).exists():
            progress = Progress(
                user=user,
                last_session=session,
                last_topic=topic,
            )

            progress.save()
        else:
            # update user progress if exists
            progress = Progress.objects.get(user=user, last_session=session)

            progress.last_session = session
            progress.last_topic = topic
            progress.save(update_fields=['last_session', 'last_topic'])

        return JsonResponse({
            'error': False,
            'message': 'Updated session'
        })
