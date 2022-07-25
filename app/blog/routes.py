from flask import Blueprint, render_template, request, jsonify, flash, redirect, url_for
from app.models import db, User, Post, load_user
from .blogforms import PostForm
from flask_login import current_user, login_required


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
            return jsonify({f'Sorry: Only {user.username} can chirp on this page'}), 403

    return render_template('userprofile.html', user=user, posts=posts, form=form)


@blog.route('/delete/<int:pid>')
@login_required
def deletePost(pid):
    to_delete = Post.query.get(pid)
    if current_user.id == to_delete.user_id:
        db.session.delete(to_delete)
        db.session.commit()
        flash('Chirp deleted successfully.', 'info')
        return redirect(url_for('blog.userProfile', username=current_user.username))
    return jsonify({"Sorry: You cannot delete another Bird Brain's chirp"}), 403


@blog.route('/users')
def users():
    if current_user.is_authenticated:
        users = User.query.filter(User.id!=current_user.id).all()
    else:
        users=User.query.all()

    return render_template('findusers.html', users=users)

@blog.route('/newsfeed')
def newsfeed():
    if current_user.is_authenticated:

        posts = current_user.followed_posts()
    else:
        posts=Post.query.order_by(Post.timestamp.desc()).all()
        

    return render_template('newsfeed.html', posts=posts)

