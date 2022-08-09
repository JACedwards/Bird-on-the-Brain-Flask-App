from __future__ import with_statement
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from flask_login import LoginManager, UserMixin
login = LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)

from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash
from secrets import token_hex

#standalone table used for user/follower relationships, not its own separate object

followers = db.Table(
    'followers',
    db.Column('follower_id', db.String, db.ForeignKey('user.id')),
    db.Column('user_id', db.String, db.ForeignKey('user.id'))
    
    )


class User(db.Model, UserMixin):
    id = db.Column(db.String(40), primary_key = True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    bio = db.Column(db.String(255), default = '(Bio)')
    fav_bird = db.Column(db.String(40), default = '(Favorite Bird)')
    password = db.Column(db.String(255), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    city = db.Column(db.String(40))
    state = db.Column(db.String(20)) 
    county = db.Column(db.String(40)) 
    birding_group = db.Column(db.String(150))
    api_token = db.Column(db.String(100)) 
    posts = db.relationship('Post', backref='author')
    followed = db.relationship(
        'User', 
        secondary=followers,
        primaryjoin=(followers.c.follower_id==id), #will find all of the users this user is following
        secondaryjoin=(followers.c.user_id==id), #will find all of the users who follow this user.
        backref=db.backref('followers')
    )

    def __init__(self, username, email, password, first_name='', last_name=''):
        self.username = username
        self.email = email.lower() 
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)
        self.api_token = str(token_hex(16))

    def follow(self, u):
        """expects a user object, follows that user"""
        
        self.followed.append(u)
        db.session.commit()

    def unfollow(self, u):
        """expects a user object, unfollows that user"""

        self.followed.remove(u)
        db.session.commit()

    def followed_posts(self):
        """ this fucionts runs database query to get all posts followed by this user, including their own posts"""
        #gets all posts by people we follow
        f_posts = Post.query.join(followers, followers.c.user_id == Post.user_id).filter(followers.c.follower_id == self.id)
        #get own posts
        own = Post.query.filter_by(user_id=self.id)
        return f_posts.union(own).order_by(Post.timestamp.desc())

    


#Twitter-related Code:  User Post-related model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(400))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.String(40), db.ForeignKey('user.id'))
    image = db.Column(db.String(500))
    
    #******use this to grab username when using table that doesn't already have username in it.********
    # *** Sam create then switch to backref in User Model****
    # ****Craig still using for Bird model on list search page

    # def getUsername(self):
    #     return User.query.get(self.user_id).username



class Bird(db.Model):
    # *****See code at bottom to help with this issue?  
    # Is ID below the same as User Id or is ti id for bird sighting row? 
    # ********** Might NEED to ADD ID of User who made this sighting******* 
    # Christopher gave me some code in slack too****

    user_id = db.Column(db.String(40))
    bird_id = db.Column(db.String(40), primary_key=True)
    common_name = db.Column(db.String(100), nullable=False)
    latin_name = db.Column(db.String(100))
    city = db.Column(db.String(60))
    county = db.Column(db.String(50))
    state = db.Column(db.String(30), nullable=False)
    date = db.Column(db.String(30))
    date_year = db.Column(db.String(5), nullable=False )
    date_month = db.Column(db.String(5) )
    date_day = db.Column(db.String(5))
    comments = db.Column(db.String(500))
    image = db.Column(db.String(500))
    #use free image hosting site; but if hosting site goes down, you are screwed
    habitat = db.Column(db.String(75))
    diet = db.Column(db.String(75))
    behaviors = db.Column(db.String(100))
    weight_g = db.Column(db.Integer)
    price =db.Column(db.Float(2))  # the number specified in the Float is the number of decimal places
    conservation = db.Column(db.String(30))
    created_on = db.Column(db.DateTime, default=datetime.utcnow())
    outing = db.Column(db.String(100))
    backyard = db.Column(db.String(10))
    annual = db.Column(db.String(10))
    lifetime = db.Column(db.String(10))

    def __init__(self, dict):
        
        self.user_id=dict.get('user_id')
        self.bird_id = str(uuid4())
        self.common_name = dict.get('common_name')
        self.county = dict.get('county')
        self.state = dict.get('state')
        #optional
        self.latin_name = dict.get('latin_name')
        self.date = dict.get('date')
        self.city = dict.get('city')
        self.comments = dict.get('comments')
        self.image = dict.get('image')
        self.habitat = dict.get('habitat')
        self.diet = dict.get('diet')
        self.behaviors = dict.get('behaviors')
        self.weight_g = dict.get('weight_g')
        self.price = dict.get('price')
        self.conservation = dict.get('conservation')
        self.outing = dict.get('outing')
        self.backyard = dict.get('backyard')
        self.annual = dict.get('annual')
        self.lifetime = dict.get('lifetime')
        self.date_year = dict.get('date_year')
        self.date_month = dict.get('date_month')
        self.date_day = dict.get('date_day')

    def getUsername(self):
        return User.query.get(self.user_id).username


class EBirdSearch(db.Model):

    country = db.Column(db.String(40), primary_key=True)  
    state = db.Column(db.String(40))  
    county = db.Column(db.String(40))  
    obsDate = db.Column(db.String(40))  
    days = db.Column(db.String(40))  
    hotspots = db.Column(db.String(40))  
    interesting = db.Column(db.String(40))  
    comName = db.Column(db.String(40))  
    checklist = db.Column(db.String(40))  
    locName = db.Column(db.String(40))  

    def __init__(self, dict):
        
        self.country = dict.get('country')  
        self.state = dict.get('state')  
        self.county = dict.get('county')  
        self.obsDate = dict.get('obsDate')  
        self.days = dict.get('days')  
        self.hotspots = dict.get('hotspots')  
        self.interesting = dict.get('interesting')  
        self.comName = dict.get('comName')  
        self.checklist = dict.get('checklist')  
        self.locName = dict.get('locName')  


class EvilCatFact(db.Model):
    refresh = db.Column(db.String(30), primary_key=True)  
    def __init__(self, dict):
        self.refresh = dict.get('refresh') 

# class AnnualList(db.Model):
#     annual = db.Column(db.String(10), primary_key=True)
#     lifetime = db.Column(db.String(10)) 
#     backyard = db.Column(db.String(10)) 
#     outing = db.Column(db.String(10))
     

#     def __init__(self, annual, lifetime, backyard, outing):
#         self.annual = annual
#         self.lifetime = lifetime 
#         self.backyard = backyard
#         self.outing = outing


class React(db.Model):
    # *****See code at bottom to help with this issue?  
    # Is ID below the same as User Id or is ti id for bird sighting row? 
    # ********** Might NEED to ADD ID of User who made this sighting******* 
    # Christopher gave me some code in slack too****

    common_name = db.Column(db.String(100), primary_key=True)
    latin_name = db.Column(db.String(100))
    image = db.Column(db.String(100))
    habitat = db.Column(db.String(75))
    diet = db.Column(db.String(75))
    pledge = db.Column(db.Integer)
    fun_fact = db.Column(db.String(150))
    conservation = db.Column(db.String(30))
    location = db.Column(db.String(75))

    def __init__(self, dict):
        
        self.common_name = dict.get('common_name')
        self.latin_name = dict.get('latin_name')
        self.image = dict.get('image')
        self.habitat = dict.get('habitat')
        self.diet = dict.get('diet')
        self.pledge = dict.get('pledge')
        self.fun_fact = dict.get('fun_fact')
        self.conservation = dict.get('conservation')
        self.location = dict.get('location')

#Jsonify object to a dictionary
    def to_dict(self):
        return {
            'common_name': self.common_name,
            'latin_name': self.latin_name,
            'image': self.image,
            'habitat': self.habitat,
            'diet': self.diet,
            'location': self.location,
            'fun_fact': self.fun_fact,
            'pledge': self.pledge,
            'conservation': self.conservation,
        }

    def from_dict(self, dict):
        for key in dict:
            getattr(self, key) 
            setattr(self, key, dict[key])

    # See below for error handling when try to update Postgress database with this Python code 
    # when this chages.  (Thiis is at minute 1:00:00 in Flask Video Day5 AM )


        



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


# Errors for updating Model from Python to Postgresql:

# Sam Davitt:	2 potential solutions to rejected database migrations
# 02:39:42	Sam Davitt:	1. delete the migrations folder and try to redo your flask db init
# 02:39:56	Sam Davitt:	2. delete the alembic table in your database (drop table statement)
# 02:40:18	Sam Davitt:	that would be for errors relating to rejected migrations based on unrelated histories or similar errors
# 02:40:54	Sam Davitt:	if you have an error about a rejected migration due to data types not matching or data not matching, you will likely have to remove any data currently in the database (such as our Fennec Fox animal)
# 02:44:45	Kristen Bieler:	I got an error that says “no module named 'api’. What am I missing?
# 02:54:21	Sam Davitt:	when changing the datatype of a serial primary key
# 02:54:39	Sam Davitt:	we must do so manually in our database as SQLAlchemy and flask-migrate always seem to fail at this specific operation
# 02:55:40	Sam Davitt:	ALTER TABLE animal ALTER COLUMN id TYPE varchar(40);
# May have to update any modify datatype of primary key column and may have to be done manually in postres database.
