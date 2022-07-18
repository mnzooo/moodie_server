import os
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\rnlgksclsrn\\.ssh\\moodie_firebase_auth_private_key.json")
default_app = firebase_admin.initialize_app(cred)

# django secret key
os.environ["SECRET_KEY"] = "django-insecure-c-i6bue*h03-4*su@bn$v++%%bu_bm7(keyru%%cs&_y#%%mw(^#*"


