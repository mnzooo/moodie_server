import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\\Users\\rnlgksclsrn\\.ssh\\moodie_firebase_auth_private_key.json")
firebase_admin.initialize_app(cred)
