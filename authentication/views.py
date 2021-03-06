import re
import logging
from datetime import datetime, timedelta
from os import getenv
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from requests import get as get_request, exceptions as requests_exceptions
from jwt import encode as encode_jwt, decode as decode_jwt
from .models import User

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)

@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse('Backend server made with Python, Hello World! Authentication APIs with Google goes here')
    elif request.method == 'POST':
        logging.info('Authenticating user login')

        # parse JSON request body
        PARAMS = {'id_token': request.body.strip()}

        # verify if JWT is from Google and get user object from Google
        try:
            r = get_request(
                url='https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=',
                params=PARAMS
            )

            r.raise_for_status()

            user_object = r.json()
            logging.info('Successfully exchanged tokeninfo with Google')
        except requests_exceptions.RequestException as error:
            logging.error('Error occured while exhcanging tokeninfo with Google', error)
            return HttpResponse(
                'Error occurred while making a request to Google, token may have expired or is malformed',
                status=error.response.status_code
            )

        # check if account is from *.edu.sg and is verified
        if not "edu.sg" in user_object['email'].split('@')[1] or not user_object['email_verified']:
            logging.warning('User logged in with non *.edu.sg account')
            return HttpResponse('Invalid email', status=401)

        google_id = user_object['sub']

        # create new record if user does not exist
        if not User.objects.filter(google_id=google_id).exists():
            logging.info('Creating new user account')

            user = User(
                google_id=google_id,
                avatar=user_object['picture'],
                email=user_object['email'],
                name=user_object['name'],
                first_name=user_object['given_name'],
                family_name=user_object['family_name']
            )

            user.save()

        # set cookie
        logging.info('Creating new JWT for cookie')


        user = User.objects.get(google_id=google_id)
        user_token = encode_jwt({
            'avatar': user.avatar,
            'name': user.name,
            'firstName': user.first_name,
            'exp': int(datetime.now().timestamp() + 1.21e+6),
            'googleId': google_id
        }, getenv('JWT_SECRET'), algorithm="HS256")

        logging.info('Sending successful user token response')
        response = HttpResponse(user_token)
        return response

    else:
        return HttpResponse('Server does not know how to handle your method', status=400)

@csrf_exempt
def get_email(request):
    if request.method != 'GET':
        return HttpResponse('Server does not know how to handle your method', status=400)

    if 'Authorization' not in request.headers:
        return HttpResponse('Missing authorization header', status=401)

    user_token = request.headers.get('Authorization');

    try:
        payload = decode_jwt(user_token, getenv('JWT_SECRET'), algorithms='HS256')
    except Exception as error:
        return HttpResponse('Invalid JWT token', status=401)

    user = User.objects.get(google_id=payload['googleId'])
    return JsonResponse({ 'email': user.email })