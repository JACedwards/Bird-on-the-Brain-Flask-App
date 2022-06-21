from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BirdForm(FlaskForm):
    common_name = StringField('Bird Name', validators=[DataRequired()])
    latin_name = StringField('Latin Name')
    date = StringField('Date', validators=[DataRequired()])
    county = StringField('County', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    comments = StringField('Notes')
    image = StringField('Image')
    submit = SubmitField()

class ListSearchForm(FlaskForm):
    user_id = StringField('User Id')
    common_name = StringField('Bird Name')
    latin_name = StringField('Latin Name')
    date = StringField('Date')
    county = StringField('County')
    state = StringField('State')
    comments = StringField('Notes')
    image = StringField('Image')
    submit = SubmitField()

class EbirdSearchForm(FlaskForm):
    country = StringField('Country')
    state = StringField('State')
    county = StringField('County')
    obsDate = StringField('Date')
    days = StringField('Days')
    hotspots = StringField('Hotspots')
    interesting = StringField('Interesting Birds')
    comName = StringField('Bird')
    checklist = StringField('Checklists')
    locName = StringField('Location')
    submit = SubmitField()