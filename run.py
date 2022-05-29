from app import app
from app.models import db, Bird, User

@app.shell_context_processor
def shell_context():
    return{'db': db, 'Bird': Bird, 'User' : User}

