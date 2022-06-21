from flask import Blueprint, jsonify, request, render_template, url_for, flash, redirect
api = Blueprint('api', __name__, url_prefix='/api')
from app.models import Bird, db, EBirdSearch
from .services import token_required
from .apiforms import BirdForm, ListSearchForm, EbirdSearchForm
from flask_login import current_user
from ebird.api import get_region, get_adjacent_regions, get_regions, get_observations
import requests as r


# leaving out validate on submit for now
@api.route('/sighting', methods=['GET', 'POST'])
def postSighting():
    bform = BirdForm()
    if request.method == 'POST':
        
        sighting=bform.data
        id=current_user.id
        sighting['user_id']=id
        # print(sighting)
        bird = Bird(sighting)
        # print(bird)
        # print(bird.user_id, bird.common_name)
        db.session.add(bird)
        db.session.commit()
        flash(f'{bird.common_name} has been added to your list.', category = 'success')        
        return redirect(url_for('api.postSighting'))
    else:
        return render_template('sighting.html', form=bform)



@api.route('/list_search', methods=['GET', 'POST'])
def internalSearch():
    # return 'This is the list search page'
    lsform = ListSearchForm()

    # *******Right now this is only set up to search Bird Sighting database by state coloumn*********
    #     Also, only tested with state that had only one row, so will need to create loop on templates page as well.

    if request.method == 'POST':
        
        ls_search=lsform.data
        print(ls_search)

        # id=current_user.id
        # sighting['user_id']=id
        search_input = Bird(ls_search)
        # the above results in state that was input into form
        search_results = Bird.query.filter_by(state=search_input.state).all()
        # print(search_results[0].common_name, search_results[1].common_name)
        # print('test')
        # print(search_results)
        # for i in search_results:
        #     print(i.state)

        
        
        
        return render_template('list_search_results.html', form = search_results) 




        # flash(f'{bird.common_name} has been added to your list.', category = 'success')        
        # return redirect(url_for('api.postSighting'))
    else:
        # return render_template('list_search', form=lssearch)
        return render_template('list_search.html', form=lsform)







@api.route('/ebird_search', methods=['GET', 'POST'])
def eBirdSearchFunction():
    
    ebform = EbirdSearchForm()

    if request.method == 'POST':
                
        eb_search=ebform.data
        # print(eb_search)  **[this prints dictionary of input]
        # print(eb_search.county, eb_search.days)

        eb_search_input=EBirdSearch(eb_search)
        # print(eb_search_input)
        # print(eb_search_input.county, eb_search_input.days)


        search_results = get_observations('bdhdkslf0ktt', f'US-IN-{eb_search_input.county}', back=eb_search_input.days)
        print(search_results)

        return render_template('ebird_search_results.html', form = search_results) 

    return render_template('ebird_search.html', form=ebform)








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
