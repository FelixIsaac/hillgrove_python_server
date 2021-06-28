import re
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
        except requests_exceptions.RequestException as error:
            return HttpResponse(
                'Error occurred while making a request to Google, token may have expired or is malformed',
                status=error.response.status_code
            )

        # check if account is from students.edu.sg and is verified
        if user_object['hd'] != 'students.edu.sg' and not user_object['email_verified']:
            return HttpResponse('', status=400)

        google_id = user_object['sub']

        # create new record if user does not exist
        if not User.objects.filter(google_id=google_id).exists():
            # get only avatar ID
            avatar = re.findall('\w{43}', user_object['picture'])[0]

            user = User(
                google_id=google_id,
                avatar=avatar,
                email=user_object['email'],
                name=user_object['name'],
                first_name=user_object['given_name'],
                family_name=user_object['family_name']
            )

            user.save()

        # set cookie
        user = User.objects.get(google_id=google_id)
        user_token = encode_jwt({
            'avatar': user.avatar_url,
            'name': user.name,
            'firstName': user.first_name,
            'exp': int(datetime.now().timestamp() + 1.21e+6)
        }, getenv('JWT_SECRET'))

        response = HttpResponse(user_token)
        return response

    else:
        return HttpResponse('Server does not know how to handle your method', status=400)
