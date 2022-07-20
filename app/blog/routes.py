from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from app.models import db, User, Post
from .blogforms import PostForm
from flask_login import current_user


blog = Blueprint('blog', __name__, template_folder='blog_templates', url_prefix='/blog')

@blog.route('/<string:username>', methods=['GET', 'POST'])
def userProfile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        posts = Post.query.filter_by(user_id=user.id).order_by(Post.timestamp.desc()).all()
    else:
        #replace with 404 redirect later
        return render_template('userprofile.html', user=None, posts=None)

    form = PostForm()
    if request.method == 'POST'and current_user.is_authenticated:
        if current_user.id == user.id:
            newpost = Post()
            newpost.body = form.new_post.data
            newpost.user_id = current_user.id
            db.session.add(newpost)
            db.session.commit()
            flash('New post successfully created', 'success')
            return redirect(url_for('blog.userProfile', username=current_user.username))

        else:
            #someone tried to post by bypassing the template
            return jsonify({f'Sorry: Only {user.username} can post on this page'}), 403

    return render_template('userprofile.html', user=user, posts=posts, form=form)