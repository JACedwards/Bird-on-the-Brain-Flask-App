
from flask import Flask
from config import Config 

app = Flask(__name__)

app.config.from_object(Config)

from . import routes  #from the "app" folder import the entire routes file


