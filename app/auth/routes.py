from flask import Blueprint, render_template, request
from .authforms import LoginForm

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')


@auth.route('/login', methods=['GET','POST'])
def login():

   
    lform = LoginForm()
###Stopped here in the forms video
###because the if clause was not working
###When filled in login form and hit submit, did not get the "thanks for logging in message below."
    if request.method == 'POST':
        print('form submitted')
        return 'Thanks for logging in.'


    return render_template('signin.html', form = lform)



