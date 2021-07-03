import re
import logging
from datetime import datetime, timedelta
from os import getenv
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from requests import get as get_request, exceptions as requests_exceptions
from jwt import encode as encode_jwt
from .models import User


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse('Backend server made with Python, Hello World! Authentication APIs with Google goes here')
    elif request.method == 'POST':
        loggin.info('Authenticating user login')

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
            loggin.info('Successfully exchanged tokeninfo with Google')
        except requests_exceptions.RequestException as error:
            loggin.error('Error occured while exhcanging tokeninfo with Google', error)
            return HttpResponse(
                'Error occurred while making a request to Google, token may have expired or is malformed',
                status=error.response.status_code
            )

        # check if account is from *.edu.sg and is verified
        if not "edu.sg" in user_object['email'].split('@')[1] or not user_object['email_verified']:
            loggin.warning('User logged in with non *.edu.sg account')
            return HttpResponse('Invalid email', status=401)

        google_id = user_object['sub']

        # create new record if user does not exist
        if not User.objects.filter(google_id=google_id).exists():
            loggin.info('Creating new user account')

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
        loggin.info('Creating new JWT for cookie')


        user = User.objects.get(google_id=google_id)
        user_token = encode_jwt({
            'avatar': user.avatar,
            'name': user.name,
            'firstName': user.first_name,
            'exp': int(datetime.now().timestamp() + 1.21e+6)
        }, getenv('JWT_SECRET'))

        loggin.info('Sending successful user token response')
        response = HttpResponse(user_token)
        return response

    else:
        return HttpResponse('Server does not know how to handle your method', status=400)
