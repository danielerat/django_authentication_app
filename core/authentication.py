import jwt
import datetime
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header

from core.models import User
from core.serializers import UserSerializer


def decode_access_token(token):
    try:
        payload = jwt.decode(token, 'access_secret', algorithms='HS256')
        return payload['user_id']
    except Exception as e:

        raise exceptions.AuthenticationFailed("Unauthenticated")


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')  # Token in string
            id = decode_access_token(token)
            user = User.objects.get(pk=id)
            return (user, None)
        raise exceptions.AuthenticationFailed("Unauthenticated")


def create_access_token(id):
    return jwt.encode(
        {
            'user_id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat': datetime.datetime.utcnow()
        }, 'access_secret', algorithm='HS256'
    )


def create_refresh_token(id):
    return jwt.encode(
        {
            'user_id': id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
            'iat': datetime.datetime.utcnow()
        }, 'access_secret', algorithm='HS256'
    )
