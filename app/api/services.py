from app.models import User
from flask import jsonify, request, flash, redirect, url_for
from functools import wraps
from ebird.api import get_region, get_adjacent_regions, get_regions, get_observations
from flask_login import current_user

def token_required(api_route):
    @wraps(api_route)
    def decorator_function(*args, **kwargs):
        token = request.headers.get('birds-access-token')
        print(current_user.api_token)
        if not token:
            return jsonify({'Access Denied':'No API token.  Please sign up to recieve your api token'}), 401
        if not User.query.filter_by(api_token=token).first():
            return jsonify({'Invalid API token': 'Please check your API token or request a new one.'}), 403
        return api_route(*args, **kwargs)
    return decorator_function





