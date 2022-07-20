from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired 

class PostForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   new_post = StringField('Chirp', validators=[DataRequired()])
   submit = SubmitField()