
from flask import Flask
from config import Config 
from .auth.routes import auth
from .api.routes import api
from .blog.routes import blog
#database imports
from .models import db, login
from flask_migrate import Migrate
from flask_cors import CORS
# from flask_mail import Mail


  

app = Flask(__name__)

app.config.from_object(Config)

CORS(app, origins='*')

app.register_blueprint(auth)
app.register_blueprint(api)
app.register_blueprint(blog)


db.init_app(app)

migrate = Migrate(app,db)

login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to see this page.'
login.login_message_category = 'danger'

#mail additions

app.config['MAIL_SERVER'] = 'stmp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'noreply.bird.brain@gmail.com'
app.config['MAIL_PASSWORD']  = 'Hurston1947#Go0Ber'

mail=Mail(app)



from . import routes  


