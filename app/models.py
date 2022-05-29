from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_login import LoginManager,UserMixin
login = LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)

from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash

class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latin_name = db.Column(db.String(100), default='Unkown')
    created = db.Column(db.DateTime, default=datetime.utcnow())
    habitat = db.Column(db.String(75))
    food = db.Column(db.String(75))
    behaviors = db.Column(db.String(100))
    weight_g = db.Column(db.Integer)
    conservation = db.Column(db.String(30))

    # Info may be found at https://www.allaboutbirds.org/guide/browse/taxonomy#
    #URL's are names are very specific names of birds
    #could do some general search categories though
    # following would take user to results for general search for "duck"
    #having lots of specific duck options
    #https://www.allaboutbirds.org/news/search/?q=duck

class User(db.Model, UserMixin):
    id = db.Column(db.String(40), primary_key = True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(200))
    created = db.Column(db.DateTime, default=datetime.utcnow())
    city = db.Column(db.String(40))
    state = db.Column(db.String(20)) 
    county = db.Column(db.String(40)) 
    birding_group = db.Column(db.String(150)) 


    def __init__(self, username, email, password):
        self.username = username
        self.email = email.lower() 
        self.password = generate_password_hash(password)
        self.id = str(uuid4())



