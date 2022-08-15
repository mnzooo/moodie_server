import os, sys
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from rest_framework import authentication
from apis.user_api.models import UserAccount
from apis.user_api.exceptions import NoAuthToken, InvalidAuthToken, FirebaseError

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

if not firebase_admin._apps:
    cred = credentials.Certificate("C:\\Users\\key\\moodie-91484-firebase-adminsdk-5znhq-a8259d48de.json")
    default_app = firebase_admin.initialize_app(cred)

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None

        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")
            pass

        if not id_token or not decoded_token:
            return None

        try:
            uid = "nMESHnruiDgZnAGHaPpMk0XduZo2"
            # decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user_uid, created = UserAccount.objects.get_or_create(user_uid=uid)
        return user_uid, None
