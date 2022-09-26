from flask import Flask
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import utils
import json

import os 
client_id = os.environ['ENV_CLIENT_ID']
client_secret = os.environ['ENV_CLIENT_SECRET']


url_token = "https://api.anbima.com.br/oauth/access-token"
token_req_payload = {'grant_type': 'client_credentials'}

token_response = requests.post(url_token,
                data=token_req_payload, verify=False, allow_redirects=False,
                auth=(client_id, client_secret))



if token_response.status_code !=200:
    print("Failed to obtain token from the OAuth 2.0 server")

tokens = json.loads(token_response.text)

headers= {'access_token': tokens['access_token'], 'client_id':client_id}
    

secrets = {
    'ANBIMA_TOKEN': headers
}