# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField


class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    selection = SelectField('University', choices=[])