# Forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField


class EventForm(FlaskForm):
    resource_type = SelectField('Selection', choices=[])
    resource_name = StringField('resource_name')
    resource_date = StringField('resource_date')
    resource_start_time = StringField('resource_start_time')
    resource_end_time = StringField('resource_end_time')
    resource_mark = StringField('resource_mark')
    # resource_file