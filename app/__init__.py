
from flask import Flask
from config import Config 
from .auth.routes import auth
#database imports
from .models import db

####FLASK_MIGRATE not recognized######
from flask_migrate import Migrate
  

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(auth)

db.init_app(app)

####MIGRATE not recogized
migrate = Migrate(app,db)




from . import routes  #from the "app" folder import the entire routes file


