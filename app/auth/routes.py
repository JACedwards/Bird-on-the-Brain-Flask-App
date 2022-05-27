from flask import Blueprint, render_template
from .authforms import LoginForm

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

#commented below out when had problems importing flask_wtf
# from .authforms import LoginForm

@auth.route('/login')
def login():
    # return 'test'
 #commented out below when having problems with flask_wtf forms.   
    lform = LoginForm()
    return render_template('signin.html', form = lform)

@auth.route('/base')
def base_test():

    return render_template('base.html')