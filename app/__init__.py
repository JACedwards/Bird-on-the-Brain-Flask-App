
from flask import Flask
from config import Config 
from .auth.routes import auth
#database imports
from .models import db
#added during import problems
from flask_migrate import Migrate
#added above during import problems  

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(auth)

#added below during import problem period
db.init_app(app)
migrate = Migrate(app,db)
#added above during import problem period



from . import routes  #from the "app" folder import the entire routes file


