import os
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\ott_project\moodie-server\moodie_firebase_auth_private_key.json")


# django secret key
os.environ["SECRET_KEY"] = "django-insecure-c-i6bue*h03-4*su@bn$v++%%bu_bm7(keyru%%cs&_y#%%mw(^#*"


