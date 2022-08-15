import os
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\key\\moodie-91484-firebase-adminsdk-5znhq-a8259d48de.json")


# django secret key
os.environ["SECRET_KEY"] = "django-insecure-c-i6bue*h03-4*su@bn$v++%%bu_bm7(keyru%%cs&_y#%%mw(^#*"


