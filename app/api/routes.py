from flask import Blueprint, jsonify, request, render_template, url_for, flash, redirect
from pkg_resources import working_set
from sqlalchemy import null
api = Blueprint('api', __name__, url_prefix='/api')
from app.models import Bird, db, EBirdSearch, EvilCatFact
from .services import token_required, getCountyByDate
from .apiforms import BirdForm, ListSearchForm, EbirdSearchForm, AnnualListForm, EvilCatFactForm
from flask_login import current_user
from ebird.api import get_region, get_adjacent_regions, get_regions, get_observations
import requests as r
import random





# leaving out validate on submit for now
@api.route('/sighting', methods=['GET', 'POST'])
# @token_required
def postSighting():
    bform = BirdForm()
    if request.method == 'POST':
        sighting=bform.data
        id=current_user.id
        sighting['user_id']=id
        bird = Bird(sighting)
        # **object comprised of form input with addition of user_id
    
        list_bird_dicts = []
        search_input=Bird.query.filter_by(common_name=bird.common_name).all()
        print(search_input)

        if search_input == []:
            bird.__dict__['annual']='annual'
            bird.__dict__['lifetime']='lifetime'
            db.session.add(bird)
            db.session.commit()


        # **probably need error handling here if query returns empty list?
        a=''
        for x in search_input:
            bird_dict = x.__dict__
            list_bird_dicts.append(bird_dict)
                     
        for x in list_bird_dicts:
            if x['annual'] == 'annual':
                a = 'annual'
                # **no change to bird (object)
            else:
                a = 'missing'

        if a == 'missing':
            bird.__dict__['annual']='annual'
            # input_annual = bird.__dict__
            # input_annual['annual']='annual'

        b=''
        # Lifetime Check Starts
        for y in list_bird_dicts:
            if y['lifetime'] == 'lifetime':
                b = 'lifetime'
            else:
                b = None

        if b == None:
            bird.__dict__['lifetime']='lifetime'

       
        print(bird.__dict__)
           
        db.session.add(bird)
        db.session.commit()

        flash(f'{bird.common_name} has been added to your lists.', category = 'success')
                
        return redirect(url_for('api.postSighting'))
    else:
        # #next three lines were my attempt to grab token from user table
        # print(current_user, current_user.api_token)
        # header = {'birds-access-token': current_user.api_token}
        # return render_template('sighting.html', form=bform, headers = header)
        return render_template('sighting.html', form=bform)






@api.route('/annual_list', methods=['GET', 'POST'])
# @token_required
def getAnnualList():
    
    
    # Do conditionals here so both annual and lifetime working_set
    # Ave for later yearfield variable to filter by year
    # For now, just cheat and only enter 2022 as samples in database
    
    galform = AnnualListForm()

    if request.method == 'POST':
        
        gal_search=galform.data
        print('this is gal_search', gal_search)
        for k , v in gal_search.items():
            if v == '':
                which_list = k
        
        if which_list == 'annual':
            search_results = Bird.query.filter_by(annual=which_list).all()
            # print('this is search results', search_results)
        elif which_list == 'lifetime':
            search_results = Bird.query.filter_by(lifetime=which_list).all()
            # print('this is search results', search_results)
        # search_input = Bird(gal_search)
        # print('this is search_input.annual', search_input.annual)
        
        
        # return 'testing'
           
        return render_template('annual_list_results.html', form = search_results,header=which_list ) 

    else:
      
        return render_template('annual_list.html', form=galform)



# ***does not throw error if user puts in bird, year, country or state that is not in database***

@api.route('/list_search', methods=['GET', 'POST'])
# @token_required
def internalSearch():
    # return 'This is the list search page'
    lsform = ListSearchForm()
    if request.method == 'POST':
        
        ls_search=lsform.data
        print(ls_search)
        for k, v in ls_search.items():
            if v != None and k != 'csrf_token' and v !='' and v != True:
                
                which_list = k
                which_list_value = v


        search_results=''
        if which_list == 'state':
            search_results = Bird.query.filter_by(state=which_list_value.title()).all()
        elif which_list == 'common_name':
            search_results = Bird.query.filter_by(common_name=which_list_value.title()).all()
            print(search_results)
        elif which_list == 'date_year':
            search_results = Bird.query.filter_by(date_year=which_list_value).all()
        elif which_list == 'county':
            search_results = Bird.query.filter_by(county=which_list_value.title()).all()

        if search_results == []:
            flash('No records found.  Please be sure to check spelling, use XXXX format for year, and/or use only one field per search.', category='danger')
            return redirect(url_for('api.internalSearch'))

        else:

            if which_list == 'common_name':
                which_list = 'Bird'
            elif which_list == 'date_year':
                which_list = 'Year'
            elif which_list == 'county':
                which_list = 'County'
            elif which_list == 'state':
                which_list = 'State'

            return render_template('list_search_results.html', form = search_results, key=which_list, value=which_list_value) 
            # flash(f'{bird.common_name} has been added to your list.', category = 'success')        
            # return redirect(url_for('api.postSighting'))
   
    else:
        # return render_template('list_search', form=lssearch)
        return render_template('list_search.html', form=lsform)


# def getCountyByDate(county_name, days):

#     """Call to API returning Bird observations for specified county ('county_name') and number of days from present backwards ('days')"""
#     county_code = get_regions('bdhdkslf0ktt', 'subnational2', 'US-IN')

#     for x in county_code:
#         if x['name'] == county_name:
#             country_state_county = x['code']

#     records = get_observations('bdhdkslf0ktt', f'{country_state_county}', back=f"{days}")
#     print
#     return records


@api.route('/ebird_search', methods=['GET', 'POST'])
def eBirdSearchFunction():
    
    ebform = EbirdSearchForm()

    if request.method == 'POST':

        try:        
            eb_search=ebform.data
            eb_search_input=EBirdSearch(eb_search)
            search_results = getCountyByDate(eb_search_input.state.title(), eb_search_input.county.title(), eb_search_input.days)
            print(search_results)
            return render_template('ebird_search_results.html', form = search_results, form_state=eb_search_input.state, form_county=eb_search_input.county, form_days=eb_search_input.days)
        except:
            flash('Records not found.  Please check state & county spelling, and be sure to enter 1-30 for days.', category='danger')
            return redirect(url_for('api.eBirdSearchFunction'))
            

    return render_template('ebird_search.html', form=ebform)


@api.route('/evil_cat', methods=['GET'])
def fetchEvilCatFact():
    
    data =''
    data = r.get('https://catfact.ninja/fact')
    data=data.json()


    data_image =''
    data_image = r.get('https://api.thecatapi.com/v1/images/search')
    data_image=data_image.json()
    print(data_image)

    birds =['Ruddy Duck', 'Peacock', 'Wren', 'Blue Jay', 'Osprey', 'Harrier', 'Buzzard', 'Vulture', 'Kite', 'Kestrel', 'Eagle', 'Hawk', 'Falcon', 'Shikra', 'Cardinal', 'Hummingbird', 'Cow Bird', 'Robin', 'Downy Woodpecker']
    bird_list=random.choice(birds)

    return render_template('evil_cat.html', form=data, image=data_image, random_bird = bird_list)

    # https://catfact.ninja/fact 
    # https://api.thecatapi.com/v1/images/search

#Trying to discover route I deleted that is needed by the react app
#Will Add here if I find it.

# SCREWED WITH THIS  and got it to work.  The change was so that jason data was a list of dictionaries.
@api.route('/birds', methods=['GET'])
def getBirds():
    birds = Bird.query.all()
    print(birds)
    birds = {a.bird_id: a.to_dict() for a in birds} 
    return jsonify(birds), 200

    # birds = [bird.to_dict() for bird in Bird.query.all()]
    # jsonify(birds.to_dict()), 200
    # return jsonify(birds), 200







 #Searching Data of Other Users   

@api.route('/other-user-search', methods=['GET', 'POST'])
# @token_required
def otherUserSearch():

    #**********<>Need to add POST route here**********************************************************

    return render_template('other-user-search.html')



# ***Old**


# @api.route('/update/<string:id>', methods = ['POST'])
# @token_required
# def updateBird(id):
#     try:    
#         newvals = request.get_json()
#         bird = Bird.query.get(id)
        
#         bird.from_dict(newvals)
#         db.session.commit()
#         return jsonify(({'Updated': bird.to_dict()})), 200

#     except:
#         return jsonify({'Request failed':'Invalid request or bird ID does not exist'}), 400


# @api.route('/delete/<string:id>', methods=['DELETE'])
# @token_required
# def removeBird(id):
#     bird = Bird.query.get(id)
#     if not bird:
#         return jsonify({'Remove failed': f"No animal exists in the database with {id}."})
#     db.session.delete(bird)
#     db.session.commit()
#     return jsonify({'Removed bird': bird.to_dict()}), 200
