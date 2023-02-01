from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User, db
from .authforms import LoginForm, RegistrationForm, ResetRequestForm, ResetPasswordForm
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, current_user, login_required, logout_user
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, TimedSerializer

import app
# from flask_mail import Message


auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')


@auth.route('/login', methods=['GET','POST'])
def login():
   
    lform = LoginForm()

    if request.method == 'POST':
        if lform.validate_on_submit():
            user = User.query.filter_by(username=lform.username.data).first()
            print(user)
            if user and check_password_hash(user.password, lform.password.data):
                login_user(user)
                print('current user:', current_user.__dict__)
                flash(f'Success -- You have been signed in, {user.username}.', category = 'success')
                return redirect(url_for('home'))

        flash(f'Incorrect username or password.  Please try again.', category = 'success')
        return redirect(url_for('auth.login'))
        
    return render_template('signin.html', form = lform)


@auth.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            newuser = User(form.username.data, form.email.data, form.password.data)
            print(newuser)

            try:
                db.session.add(newuser)
                db.session.commit()
            except:
                flash('Username or email already taken.  Please try a different ones.', category='danger')
                return redirect(url_for('auth.register'))

            login_user(newuser)
            flash(f'Welcome, {newuser.username}! Thank you for signing up!', category = 'info')
            return redirect(url_for('home'))
        else:
            flash("Sorry, your passwords don't match.  Please try again.", category = 'danger')
            return redirect(url_for('auth.register'))

    elif request.method == 'GET':
        return render_template('register.html', form=form)


    
    # <!-- ---------------------------starting to work on reset   **ready to start on email through Itsdangerous

    # (Using this video here; was using another video in routes)
    # https://www.youtube.com/watch?v=zYWpEJAHvaI (currently at minute 50:00 (getting error:  "socket.gaierror: [Errno 11002] getaddrinfo failed" when try to input an email on the auth/reset_passwword page.  Might be some port issues in __init__.py. also might be app.mail command. It is different from video, but couldn't see where video was ever calling the mail.send function ))
    # 
    # IF WANT TO DEPLOY, need to make the Forgot Password button on login page go away.  I think that will hide all the other pages--
    # (Once figure out, need to update beanstalk / docker version)>



# def send_mail(user):
#     print('send_mail function activated')
#     token=user.get_token()
#     msg=Message('Password Reset Request', recipients=[user.email],
#     sender='noreply.bird.brain@gmail.com') 
#     msg.body = f''' To reset your password, please follow the link below
#     print(f'this is token: {token}. and this is message body: {msg.body})

#     {url_for('auth.reset_token', token=token,_external=True)}

#     If you didn't send a password request, please ignore this email.
#     ''' 
#     app.mail.send(msg) 


# @auth.route('/reset_password', methods=['GET','POST'])
# def reset_request():
#     form=ResetRequestForm()

#     if request.method == 'POST':
#         print('Post method')
#         if form.validate_on_submit():
#             user=User.query.filter_by(email=form.email.data).first()
#             if user:
#                 send_mail(user)
#                 print('send_mail')

#                 flash(f'Reset request sent. Please, check your email.', category = 'success')
#                 return redirect(url_for('auth.login', form=None))
#     return render_template('reset_request.html', title='Reset Request', form=form)


# @auth.route('/reset_password/<token>', methods=['GET','POST'])
# def reset_token(token):
#     user=User.verify_token(token)
#     if user is None:
#         flash('You are attempting to use an invalid or expired token. Please try again.', category='warning')
#         return redirect(url_for('auth.reset_request', form=None)) #may need to remove auth.
#     form=ResetPasswordForm()
#     if form.validate_on_submit():
#         hashed_password = generate_password_hash(form.password.data)
#         #Had done password differently in models.py so adapted above
#         #this is what video actually had
#         #hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         user.password=hashed_password
#         db.session.commit()
#         flash('Password successfully changed! Please login.', category='success')        
#         return redirect(url_for('auth.login'))
#     return render_template('change_password.html', form=form)
    




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been signed out.', category = 'info')
    return redirect(url_for('auth.login'))

