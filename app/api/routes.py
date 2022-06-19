from flask import Blueprint, jsonify, request, render_template, url_for
api = Blueprint('api', __name__, url_prefix='/api')
from app.models import Bird, db
from .services import token_required
from .apiforms import BirdForm

@api.route('/sighting')
def postSighting():
    bform = BirdForm()
    return render_template('sighting.html', form=bform)




# SCREWED WITH THIS WRAp and got it to work.  The change was so that jason data was a list of dictionaries.
@api.route('/birds', methods=['GET'])
def getBirds():
    # birds = Bird.query.all()
    # print(birds)
    birds = [bird.to_dict() for bird in Bird.query.all()]

    return jsonify(birds), 200

@api.route('/bird/<string:name>', methods=['GET'])
def getAnimalName(name):
    #dynamic routing
    print(name)
    bird = Bird.query.filter_by(common_name=name.title()).first()
    if bird:
        return jsonify(bird.to_dict()), 200
    return jsonify({'error':f"{name.title()} is not present in the database"}), 404

@api.route('/create', methods=['POST'])
@token_required
def createBird():
    try:
        newdict = request.get_json()
        print(newdict)
        a = Bird(newdict)
    except:
        return jsonify({'error': 'improper body data or request'}), 400
    try:
        db.session.add(a)
        db.session.commit()
    except:
        return jsonify({'error':'Bird already exists in database'}), 400

    return jsonify({'created':a.to_dict()}), 200

@api.route('/update/<string:id>', methods = ['POST'])
@token_required
def updateBird(id):
    try:    
        newvals = request.get_json()
        bird = Bird.query.get(id)
        
        bird.from_dict(newvals)
        db.session.commit()
        return jsonify(({'Updated': bird.to_dict()})), 200

    except:
        return jsonify({'Request failed':'Invalid request or bird ID does not exist'}), 400


@api.route('/delete/<string:id>', methods=['DELETE'])
@token_required
def removeBird(id):
    bird = Bird.query.get(id)
    if not bird:
        return jsonify({'Remove failed': f"No animal exists in the database with {id}."})
    db.session.delete(bird)
    db.session.commit()
    return jsonify({'Removed bird': bird.to_dict()}), 200
