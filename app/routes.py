# 
from app import app

from flask import render_template


@app.route('/')

def home():
    birds = ['Junco', 'Blue Bird', 'Hawk']
    return render_template('index.html', birds=birds)

@app.route('/signup')

def signup():
    signup = 'Signup'
    return render_template('signup.html', signup = signup)

@app.route('/backyard_list')

def backyard_list():
    backyard = 'Backyard List'
    return render_template('backyard_list.html', backyard = backyard)    


