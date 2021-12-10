from flask_wtf import FlaskForm
from wtforms import StringField


class AnnouncementForm(FlaskForm):
    new_announcement_desc = StringField('new_announcement_desc')