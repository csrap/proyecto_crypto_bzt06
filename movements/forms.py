from sqlite3.dbapi2 import IntegrityError
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, FloatField, SubmitField, ValidationError
from wtforms import validators
from wtforms.fields.core import DecimalField, SelectField, TimeField
from wtforms.validators import DataRequired, Length, InputRequired, NumberRange
from datetime import date, datetime, timezone


coin = ('EUR', 'BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX')

class MovementForm(FlaskForm):
    from_currency = SelectField('From', choices = coin)
    from_cantidad = FloatField('from_cantidad', validators= [NumberRange(min=0.00000001, max=1000000000, message= "Cantidad no válida")]) 
    to_currency = SelectField('To', choices = coin)
    to_cantidad = DecimalField('To_cantidad')
    precio_unitario = DecimalField ('Precio Unitario')
    calculadora = SubmitField ('Calcular')
    guardar = SubmitField ('INVERTIR')

class Status_Form(FlaskForm): 
    invertido = DecimalField('Invertido')
    valor_actual = DecimalField('Valor_Actual')



