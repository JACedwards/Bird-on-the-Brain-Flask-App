from flask_wtf import FlaskForm
from wtforms import Stringfield, Passwordfield, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
   username = Stringfield('Username', validators=[DataRequired()])
   password = Passwordfield('Password', validators=[DataRequired()])
   submit = SubmitField()
