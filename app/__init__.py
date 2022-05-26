#backbone of flask app
# all other pieces must connect back to this file
#hub of all communication between independent ppieces of falsk app
#import flask object

from flask import Flask
#from config file import the config class we created
from config import Config 

#instantiate the object that will be our flask app

app = Flask(__name__)

# tell this app how it is going to be configured
app.config.from_object(Config)

# aka configuring our flask app based on the Config class we made in the config.py file

# at bottom of file something needed
# our flask app is dumb.  if we don't tell it about other files
# it asume they don't exist
# import foutes file so that our Flask app knws the routs exsit
# rare instance where imports are at bottom because must be after the instantiation of the flask ap (line 12)
    #and the configuration (line 15)
from . import routes  #from the "app" folder import the entire routes file


