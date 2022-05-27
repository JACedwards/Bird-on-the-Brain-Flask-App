from flask import Blueprint

auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

@auth.route('/login')
def login():
    return 'testing'