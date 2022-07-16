from flask import Blueprint, render_template
from app.models import db, User, Post

blog = Blueprint('blog', __name__, template_folder='blog_templates', url_prefix='/blog')

@blog.route('/<string:username>')
def userProfile(username):

    user = User.query.filter_by(username=username).first()
    if user:
        posts = Post.query.filter_by(user_id=user.id).all()
    else:
        posts = None

    return render_template('userprofile.html', user=user, posts=posts)