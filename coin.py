import requests
from config import*
from datetime import date
from datetime import datetime
from flask import render_template, request, redirect, url_for
import json 

url = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount=10000&symbol=EUR&convert=BTC&CMC_PRO_API_KEY=7fe0933d-6fd8-4d55-86ac-241f5495d96e"

print(str(url))

def peticion(url):
        respuesta = request.get(url) 
        if respuesta.status_code == 200:
                datos = respuesta.json() 
                return(datos)

amount = '10000'
symbol = 'EUR'
convert = 'BTC'
respuesta = peticion (url.format(amount, symbol, convert, API_KEY))



'''
respuesta = requests.get(url_coin.format(amount, symbol, convert, API_KEY))

if respuesta.status_code == 200:
        datos = respuesta.json() 
        print(datos)
        convert_ = datos ['data'] ['quote'] [convert] ['price']
        print(str(convert_))               
'''

