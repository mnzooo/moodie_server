import argparse
import configparser
import json
import os

import requests
from firebase_admin import auth

config = configparser.ConfigParser()
config.read('../config.ini', encoding='UTF-8')

# API_KEY = config['FIREBASE']['API_KEY'].strip()
API_KEY = "AIzaSyAwq3lUeI8eTYBPmacNcVo0ZlMbl4y5qAw"

def get_id_token(uid):

    token = auth.create_custom_token(uid)

    data = {
        'token': token,
        'returnSecureToken': True
    }

    url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty" \
          "/verifyCustomToken?key={}".format(API_KEY)

    response = requests.post(url,
                             data,
                             {'Content-Type': 'application/json'})
    response = response.json()
    id_token = response["idToken"]

    return id_token