import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects


url_price = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'


headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '7fe0933d-6fd8-4d55-86ac-241f5495d96e', 
}

session = Session()
session.headers.update(headers)

convert = {
    'amount':'1',
    'id':'1',
    'convert': 'EUR',
}
try:
    response = session.get(url_price, params=convert) # params=parameters
    data_2 = json.loads(response.text)
    symbol_crypto = data_2 ['data']['symbol']
    credit_count = data_2['data']['quote']['EUR']['price']
    print('El valor Actual de:'+ str(symbol_crypto)+' '+'es:'+  str(credit_count))
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)