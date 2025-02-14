from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.valitadors import DataRequired, Email, Equalto, Length, NumberRange, Regexp
from wtforms import StringField, EmailField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField

class UserForm(Form):
    matricula=StringField("Matricula")
    edad=IntegerField("Edad")
    nombre=StringField("Nombre")
    apellidos=StringField("Apellidos")
    email=EmailField("Email")
