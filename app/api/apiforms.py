from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class BirdForm(FlaskForm):
    common_name = StringField('Bird Name', validators=[DataRequired()])
    latin_name = StringField('Latin Name')
    # date_year = db.Column(db.String(5), nullable=False )
    # date_month = db.Column(db.String(5), nullable=False )
    # date_day = db.Column(db.String(5), nullable=False )
    date = StringField('Date')
    date_year = StringField('Year', validators=[DataRequired()])
    date_month = StringField('Month')
    date_day = StringField('Day')
    county = StringField('County')
    state = StringField('State', validators=[DataRequired()])
    comments = StringField('Notes')
    image = StringField('Image')
    submit = SubmitField()

class ListSearchForm(FlaskForm):
    user_id = StringField('User Id')
    common_name = StringField('Bird Name')
    latin_name = StringField('Latin Name')
    date_year = StringField('Year')
    county = StringField('County')
    state = StringField('State')
    comments = StringField('Notes')
    image = StringField('Image')
    backyard = StringField('Backyard')
    annual = StringField('Annual')
    lifetime = StringField('Lifetime')
    outing = StringField('Outing')
    other_user = StringField('Fellow Bird Brain')
    submit = SubmitField()

class EbirdSearchForm(FlaskForm):
    country = StringField('Country')
    state = StringField('State', validators=[DataRequired()])
    county = StringField('County', validators=[DataRequired()])
    obsDate = StringField('Date')
    days = StringField('Days', validators=[DataRequired()])
    hotspots = StringField('Hotspots')
    interesting = StringField('Interesting Birds')
    comName = StringField('Bird')
    checklist = StringField('Checklists')
    locName = StringField('Location')
    submit = SubmitField()

class AnnualListForm(FlaskForm):
    annual = StringField('Annual') 
    lifetime = StringField('Lifetime')
    backyard = StringField('Backyard')
    outing = StringField('Outing')
    all = StringField('All My Sightings')  #added so can add this to lifetime/annual page / haven't done db migrate
    submit = SubmitField()

class EvilCatFactForm(FlaskForm):
    refresh = StringField('Refresh')
    submit = SubmitField()