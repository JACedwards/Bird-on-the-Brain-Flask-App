from flask import Blueprint, jsonify
api = Blueprint('api', __name__, url_prefix='/api')
from app.models import Bird

@api.route('/test', methods=['GET'])
def test():
    junco = Bird.query.all()[1]
    return jsonify(junco.to_dict()), 200

