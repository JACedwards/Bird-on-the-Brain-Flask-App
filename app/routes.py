# flask routes control what content is shown on what URL
    # depending on how the user is accessing the URL (methods), what buttons they've pressed, or what requests they've made, what their permissions are

#general structure of a flask route is a function with a decorator
#decoratoer addes another fucntion that run before and/or after, the function being decorated

#our first route:
    # just display 'hello world' on our local host url (when we run locally, it will default run on the follwing url
    #  http://127.0.0.1:5000/
    # 
# to set up route need:
#   access to flask object
# 
from app import app

from flask import render_template

# a route decorator will follow this syntax
    #@<flask object/bluprint name>.route('url endpoint', <methods are optional>)
    # followed by a regular python function
    # return value of the python function will be displayed on the browser

@app.route('/')

def home():
    #this is a regular python function, can write normal Python code here
    birds = ['Junco', 'Blue Bird', 'Hawk']
    #return value is what is dispayed on browser
    return render_template('index.html', birds=birds)

@app.route('/signup')

def signup():
    #this is a regular python function, can write normal Python code here
    signup = 'Signup'
    #return value is what is dispayed on browser
    return render_template('signup.html', signup = signup)

@app.route('/backyard_list')

def backyard_list():
    #this is a regular python function, can write normal Python code here
    backyard = 'Backyard List'
    #return value is what is dispayed on browser
    return render_template('backyard_list.html', backyard = backyard)    

#run in terminal type command flask run

