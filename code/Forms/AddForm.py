from flask_wtf import FlaskForm
from wtforms import SelectField, StringField

class AddForm(FlaskForm):
    name = StringField('name')
    selection = SelectField('Selection', choices=[])