from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from datetime import datetime

class Bird(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    latin_name = db.Column(db.String(100), default='Unkown')
    created = db.Column(db.DateTime, default=datetime.utcnow())
    realm = db.Column(db.String(50))
    habitat = db.Column(db.String(75))
    feeding = db.Column(db.String(75))
    fledge_days = db.Column(db.Integer)
    weight_g = db.Column(db.Integer)
    life_exp = db.Column(db.Integer)


