from app import app
from app.models import db, Bird, User, Post

@app.shell_context_processor
def shell_context():
    return{'db': db, 'Bird': Bird, 'User' : User, 'Post': Post}

