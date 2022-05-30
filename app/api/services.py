from app.models import User
from flask import jsonify, request
from functools import wraps

def token_required(api_route):
    @wraps(api_route)
    def decorator_function(*args, **kwargs):
        token = request.headers.get('birds-access-token')
        if not token:
            return jsonify({'Access Denied':'No API token.  Please sign up to recieve your api token'}), 401
        if not User.query.filter_by(api_token=token).first():
            return jsonify({'Invalid API token': 'Please check your API token or request a new one.'}), 403
        return api_route(*args, **kwargs)
    return decorator_function
