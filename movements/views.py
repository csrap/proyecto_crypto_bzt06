from sqlite3.dbapi2 import Time
from flask.helpers import url_for
from movements import app 
from flask import render_template, request, redirect, url_for
import sqlite3 
from movements.forms import MovementForm
from datetime import date, timezone, datetime
from config import*
import requests

#DBFILE = app.config ['DBFILE']

@app.route('/')
def listaIngresos():
    form = MovementForm()
    conn = sqlite3.connect('movements/Data/basededatos.db')
    c = conn.cursor()

    c.execute('SELECT date, time, from_currency, form_quantity, to_currency, to_quantity, precio FROM movimientos;')

    ingresos = c.fetchall()
    

    conn.close()

    return render_template("movimientos.html", datos=ingresos, form = form)
    

@app.route('/purchase', methods=['GET', 'POST'])
def nuevaCompra():
    form = MovementForm() 
    if request.method == 'POST':

        conn = sqlite3.connect('movements/Data/basededatos.db')
        c = conn.cursor()

        c.execute('INSERT INTO movimientos (date, time, from_currency, form_quantity,to_currency, to_quantity, precio) VALUES (?, ?, ? , ? , ? , ?, ?);',       
            (
                    request.form.get('date'),
                    request.form.get('time'),
                    request.form.get('from_currency'),
                    request.form.get('form_quantity'),
                    request.form.get('to_currency'),
                    request.form.get('to_quantity'), 
                    request.form.get('precio')
            )
        )

        conn.commit()
        conn.close() 
        
        return redirect(url_for('listaIngresos'))
    
    #date, time
    today = date.today() 
    today_2 = "{}/{}/{}".format(today.day, today.month, today.year)
    now = datetime.now() 
    time = "{}:{}:{}".format(now.hour, now.minute,now.second)

    #Cantidad de Crypto Moneda
    amount = "cuanto"
    symbol = "from_currency"
    convert = "to_currency" 
    cantidad_2 = 0 

    url_coin = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY={}"

    respuesta = requests.get(url_coin.format(amount, symbol, convert, API_KEY))

    if respuesta.status_code == 200:
            datos = respuesta.json() 
            print(datos)
            cantidad_2 = datos ['data'] ['quote'] [convert] ['price']
            print(str(cantidad_2))

    return render_template("purchase.html", form = form, today_2 = today_2, time = time, amount = amount, symbol = symbol, convert = convert, cantidad_2 = cantidad_2 )

@app.route('/calculadora')
def calculo():
    return render_template("purchase.html")

@app.route('/status')
def Estado_Inversion():
    return render_template ("status.html")
