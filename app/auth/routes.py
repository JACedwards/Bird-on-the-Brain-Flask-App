from flask import Blueprint, render_template, request, redirect, url_for, flash
from .authforms import LoginForm, RegistrationForm

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')


@auth.route('/login', methods=['GET','POST'])
def login():
   
    lform = LoginForm()

    if request.method == 'POST':
        if lform.validate_on_submit():
           username = lform.username.data
           password = lform.password.data
           print('formdata:', username, password)
           flash(f'Success -- You have been signed in, {username}.', 'success')
           return redirect(url_for('home'))
        else:
            return redirect(url_for('auth.login'))
        
    return render_template('signin.html', form = lform)

@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print(form.data)
            flash('Welcome! Thank you for registering!', 'info')
            return redirect(url_for('home'))
        else:
            flash('Sorry, that username or email is taken.  Please try again.', 'danger')
            return redirect(url_for('auth.register'))

    return render_template('register.html', form=form)

