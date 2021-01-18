import requests
from config import*
from datetime import date
from datetime import datetime

amount = input("¿Cuanto quieres Invertir?")
symbol = input("¿Ingresa Moneda ? ")
convert = input ("¿Cúal Moneda quieres Convertir?")

url_coin = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY={}"

respuesta = requests.get(url_coin.format(amount, symbol, convert, API_KEY))

if respuesta.status_code == 200:
        datos = respuesta.json() 
        print(datos)
        convert_ = datos ['data'] ['quote'] [convert] ['price']
        print(str(convert_))
        
                
#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print("La hora actual es {}:{}".format(now.hour, now.minute))


