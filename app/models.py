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
    api_token = db.Column(db.String(100)) 


    def __init__(self, username, email, password):
        self.username = username
        self.email = email.lower() 
        self.password = generate_password_hash(password)
        self.id = str(uuid4())

class Bird(db.Model):
    # *****See code at bottom to help with this issue?  
    # Is ID below the same as User Id or is ti id for bird sighting row? 
    # Might NEED to ADD ID of User who made this sighting 
    # Christopher gave me some code in slack too****

    bird_id = db.Column(db.String(40), primary_key=True)
    common_name = db.Column(db.String(100), nullable=False, unique=True)
    latin_name = db.Column(db.String(100))
    city = db.Column(db.String(60))
    county = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    date = db.Column(db.DateTime, nullable=False )
    comments = db.Column(db.String(500))
    image = db.Column(db.String(500))
    #use free image hosting site; but if hosting site goes down, you are screwed
    habitat = db.Column(db.String(75))
    diet = db.Column(db.String(75))
    behaviors = db.Column(db.String(100))
    weight_g = db.Column(db.Integer)
    price =db.Column(db.Float(2))
    conservation = db.Column(db.String(30))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())


    def __init__(self, dict):
        self.bird_id = str(uuid4())
        self.common_name = dict['common_name'].title()
        self.county = dict['county'].title()
        self.state = dict['state'].title()
        self.date = dict['date']
        #optional
        self.latin_name = dict.get('latin_name')
        self.city = dict.get('city')
        self.comments = dict.get('comments')
        self.image = dict.get('image')
        self.habitat = dict.get('habitat')
        self.diet = dict.get('diet')
        self.behaviors = dict.get('behaviors')
        self.weight_g = dict.get('weight_g')
        self.price = dict.get('price')
        self.conservation = dict.get('conservation')

#Jsonify object to a dictionary
    def to_dict(self):
        return {
            'bird_id': self.bird_id,
            'common_name': self.common_name,
            'country,': self.county,
            'state': self.state,
            'date': self.date,
            'latin_name': self.latin_name,
            'city': self.city,
            'comments': self.comments,
            'image': self.image,
            'habitat': self.habitat,
            'diet': self.diet,
            'behaviors': self.behaviors,
            'weight_g': self.weight_g,
            'price': self.price,
            'conservation': self.conservation,
            'created_on' : self.created_on
        }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key) 
            setattr(self, key, dict[key])


        



    # Info may be found at https://www.allaboutbirds.org/guide/browse/taxonomy#
    #URL's are names are very specific names of birds
    #could do some general search categories though
    # following would take user to results for general search for "duck"
    #having lots of specific duck options
    #https://www.allaboutbirds.org/news/search/?q=duck


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     pub_date = db.Column(db.DateTime, nullable=False,
#         default=datetime.utcnow)

#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
#         nullable=False)
#     category = db.relationship('Category',
#         backref=db.backref('posts', lazy=True))

#     def __repr__(self):
#         return '<Post %r>' % self.title


# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), nullable=False)

#     def __repr__(self):
#         return '<Category %r>' % self.name

