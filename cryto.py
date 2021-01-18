from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url_price = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion' # cambio

url_crypto = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map' 

#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '7fe0933d-6fd8-4d55-86ac-241f5495d96e', 
}

session = Session()
session.headers.update(headers)

parameters = {
    'start':'1',
    'limit':'10',
    'sort':'id',
}

try:
    # crytomoney = input("¿Cual Crytomoneda")
    response = session.get(url_crypto,params=parameters) # params=parameters
    data_1 = json.loads(response.text)
    print(data_1)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

# cambio de crytos 

convert = {
    'amount':'1',
    'id':'1',
    'convert': 'EUR',
}

try:
    response = session.get(url_price,params=convert) # params=parameters
    data_2 = json.loads(response.text)
    print(data_2)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)