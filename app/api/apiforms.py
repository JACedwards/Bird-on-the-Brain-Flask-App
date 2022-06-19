from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BirdForm(FlaskForm):
    common_name = StringField('Common Name', validators=[DataRequired()])
    latin_name = StringField('Latin Name')
    county = StringField('County', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    image = StringField('Image')
    submit = SubmitField()
