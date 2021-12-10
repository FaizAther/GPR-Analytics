from flask_wtf import FlaskForm
from wtforms import SelectField, StringField

class AddForm(FlaskForm):
    name = StringField('name')
    type_selection = SelectField('Type', choices=[])
    selection = SelectField('Selection', choices=[])