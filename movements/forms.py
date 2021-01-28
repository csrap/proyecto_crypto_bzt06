from sqlite3.dbapi2 import IntegrityError
from flask_wtf import FlaskForm
from wtforms import IntegerField, DateField, StringField, FloatField, SubmitField, ValidationError
from wtforms import validators
from wtforms.fields.core import DecimalField, SelectField, TimeField
from wtforms.validators import DataRequired, Length, EqualTo, InputRequired
from datetime import date, datetime, timezone

def validate_staff(form, field):
    if field.data == "to_currency":
        raise ValidationError("")
    
def must_contain_one_digit(form, field):
    for c in '0123456789':
        if c in field.data:
            return None
    raise ValidationError('Debe contener al menos un número')


coin = ('EUR', 'BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX')

class MovementForm(FlaskForm):
    id = IntegerField('id')
    from_currency = SelectField('From', validators= [DataRequired('Selecciona Moneda'), EqualTo('to_currency', message='Monedas deben ser Diferentes')], choices = coin)
    from_cantidad = DecimalField('from_cantidad', validators= [DataRequired(), Length(min=3, max=12, message="El concepto debe tener más de 10 caracteres")]) 
    to_currency = SelectField('To', validators=[DataRequired('Selecciona Moneda a Convertir')], choices = coin)
    to_cantidad = DecimalField('To_cantidad')
    precio_unitario = DecimalField ('Precio Unitario')

    
    calculadora = SubmitField ('Calcular')
    guardar = SubmitField ('Guardar')

    invertido = DecimalField('Invertido')
    valor_actual = DecimalField('Valor_Actual')



