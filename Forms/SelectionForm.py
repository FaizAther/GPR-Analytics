from flask_wtf import FlaskForm
from wtforms import SelectField

class SelectionForm(FlaskForm):
    selection = SelectField('Selection', choices=[])