from sqlite3.dbapi2 import Time
from flask.helpers import url_for
import requests
from movements import app 
from flask import render_template, request, redirect, url_for
import sqlite3 
from movements.forms import MovementForm
from datetime import date, timezone, datetime
from config import*
from prueba import today_2, time 

#DBFILE = app.config ['DBFILE']
url_coin = "https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY={}"

def peticion(url):
    respuesta = requests.get(url) 
    if respuesta.status_code == 200:
        datos = respuesta.json() 
        return datos

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

        
        if form.calculadora.data == True:
            amount = form.from_cantidad.data
            symbol = form.from_currency.data
            convert = form.to_currency.data
            respuesta = peticion(url_coin.format(amount, symbol, convert, API_KEY))
            cantidad_coin = respuesta['data']['quote'][convert]['price']

            pu = float(amount) / float(cantidad_coin)

            api_coin = [amount, symbol, convert, cantidad_coin,pu]


            return render_template("purchase_coin.html", form = form, api_coin = api_coin)
        else: 
                    conn = sqlite3.connect('movements/Data/basededatos.db')
                    c = conn.cursor()
                    
                    c.execute('INSERT INTO movimientos (date, time, from_currency, form_quantity,to_currency, to_quantity, precio) VALUES (?, ?, ? , ? , ? , ?, ?);',       
                                (
                                    today_2,
                                    time,
                                    form.from_currency.data,
                                    float(form.from_cantidad.data),
                                    form.to_currency.data,
                                    float(form.to_cantidad.data), 
                                    float(form.precio_unitario.data)
                                ))

                    conn.commit()
                    conn.close() 
                    
                    return redirect(url_for('listaIngresos'))

    return render_template("purchase.html", form = form)


@app.route('/status', methods =['GET'])
def Estado_Inversion():
    form = MovementForm()
    conn = sqlite3.connect("movements/data/basededatos.db")
    c = conn.cursor()

    c.execute('SELECT SUM(to_quantity) AS total, to_currency FROM movimientos WHERE from_currency = "EUR" GROUP BY to_currency')
    ingresos = c.fetchall()

    c.execute('SELECT SUM(form_quantity) AS total, from_currency FROM movimientos WHERE from_currency="EUR"')
    ingresos2 = c.fetchone()[0]

    conn.close()
    total = 0

    for ingreso in ingresos:
        respuesta = peticion(url_coin.format(ingreso[0], ingreso[1],"EUR", API_KEY))
        total += float(respuesta['data']['quote']['EUR']['price'])

    return render_template ("status.html", form = form, valor_invertido= ingresos2, valor_actual=total)
