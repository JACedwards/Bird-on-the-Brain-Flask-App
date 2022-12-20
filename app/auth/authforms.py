from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo


class LoginForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   password = PasswordField('Password', validators=[DataRequired()])
   submit = SubmitField()

class RegistrationForm(FlaskForm):
   username = StringField('Username', validators=[DataRequired()])
   email = StringField('Email', validators=[DataRequired()])
   first_name = StringField('First Name')
   last_name = StringField('Last Name')
   city = StringField('City')
   state = StringField('State')
   county = StringField('County')
   birding_group = StringField('Birding Group')
   password = PasswordField('Password', validators=[DataRequired()])
   confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
   submit = SubmitField()

class ResetRequestForm(FlaskForm):
   email = StringField('Email', validators=[DataRequired()])
   submit = SubmitField('Reset Password')

class ResetPasswordForm(FlaskForm):
   password = PasswordField('Password', validators=[DataRequired()])
   confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
   submit = SubmitField()