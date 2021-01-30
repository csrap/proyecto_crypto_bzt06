import sqlite3
from config import*
from movements import app

DBFILE = app.config['DBFILE'] 

# dejarlo en una sola funcion 
def consulta(query, params=()):

    conn = sqlite3.connect(DBFILE)
    c = conn.cursor()

    c.execute(query, params)
    conn.commit() 


    filas = c.fetchall()


    conn.close()


    if len(filas) == 0:
        return filas

    columnNames = []
    for columnName in c.description:
        columnNames.append(columnName[0])

    listaDeDiccionarios = []

    for fila in filas:
        d = {}
        for ix, columnName in enumerate(columnNames):
            d[columnName] = fila[ix]
        listaDeDiccionarios.append(d)

    return listaDeDiccionarios

# Variable para  sacar saldo de monedas
def monedas_activas(): 

    cryto_money = ['BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX']

    movimientos = consulta('SELECT from_currency,form_quantity, to_currency, to_quantity  FROM movimientos;')

    lista_from = ['EUR']

    counter_cantidad = 0 

    for i in movimientos: 
        if i['to_currency'] != 'EUR' and i['to_currency'] not in lista_from:
            lista_from.append(i['to_currency'])
    return lista_from 


        


