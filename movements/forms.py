from sqlite3.dbapi2 import IntegrityError
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, FloatField, SubmitField, ValidationError
from wtforms import validators
from wtforms.fields.core import DecimalField, SelectField, TimeField
from wtforms.validators import DataRequired, Length
from datetime import date, datetime, timezone

coin = ('EUR', 'BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX')

class MovementForm(FlaskForm):
    id = IntegerField('id')
    from_currency = SelectField('From', validators= [DataRequired('Selecciona Moneda')], choices = coin)
    from_cantidad = DecimalField('from_cantidad', validators= [DataRequired('Solo Numeros')])
    to_currency = SelectField('To', validators=[DataRequired('Selecciona Moneda a Convertir')], choices = coin)
    to_cantidad = DecimalField('To_cantidad')
    precio_unitario = DecimalField ('Precio Unitario')
    date = DateField('date')
    time = TimeField ('time')

    Guardar = SubmitField ('Guardar')

    Invertido = DecimalField('Invertido')
    Valor_Actual = DecimalField('Valor_Actual')



