from flask import Flask
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import utils
import json

from .secrets import secrets
  
headers = secrets.get('ANBIMA_TOKEN')


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/v1/cota')
def get_anbima():
    dt_referencia = datetime.today().strftime('%Y-%m-%d')

    url = "https://api-sandbox.anbima.com.br/feed/precos-indices/v1/indices/resultados-intradiarios-ima?indice_intradiario=1&data_referencia={}".format(dt_referencia)
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, 'html.parser')
    
    return soup.prettify()
