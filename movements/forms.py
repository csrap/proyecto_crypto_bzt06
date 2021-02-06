from sqlite3.dbapi2 import IntegrityError
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, FloatField, SubmitField, ValidationError
from wtforms import validators
from wtforms.fields.core import DecimalField, SelectField, TimeField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from datetime import date, datetime, timezone
from movements.db_ejec import moneda_saldo_total 



coin = ('EUR', 'BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX')

def validar_select(form, field):
    if form.from_currency.data == form.to_currency.data:
            raise ValidationError('Error:Monedas Iguales')

def validar_saldo(form, field):
    saldo_total = moneda_saldo_total()
    if form.from_currency.data == 'EUR':
        pass
    elif field.data > saldo_total[form.from_currency.data]:
        raise ValidationError('Error: No tienes Saldo')

            

class MovementForm(FlaskForm):
    from_currency = SelectField('From',choices = coin, validators=[validar_select])
    from_cantidad = FloatField('from_cantidad', validators= [DataRequired(), NumberRange(min=0.00000001, max=1000000000, message= "Error: Cantidad no válida"),validar_saldo]) 
    to_currency = SelectField('To', choices = coin)
    to_cantidad = DecimalField('To_cantidad')
    precio_unitario = DecimalField ('Precio Unitario')
    calculadora = SubmitField("")
    guardar = SubmitField ('INVERTIR')


class Status_Form(FlaskForm): 
    invertido = DecimalField('Invertido')
    valor_actual = DecimalField('Valor_Actual')




