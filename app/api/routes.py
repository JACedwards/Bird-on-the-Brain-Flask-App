from flask import Blueprint, jsonify, request, render_template, url_for, flash, redirect
from pkg_resources import working_set
from sqlalchemy import null
api = Blueprint('api', __name__, url_prefix='/api')
from app.models import Bird, db, EBirdSearch, EvilCatFact, React
from .services import token_required
from .apiforms import BirdForm, ListSearchForm, EbirdSearchForm, AnnualListForm, EvilCatFactForm
from flask_login import current_user, login_required
from ebird.api import get_region, get_adjacent_regions, get_regions, get_observations
import requests as r
import random
import json
from datetime import datetime





# leaving out validate on submit for now
@api.route('/sighting', methods=['GET', 'POST'])
@login_required
def postSighting():
    bform = BirdForm()
    if request.method == 'POST':
        sighting=bform.data
        id=current_user.id
        sighting['user_id']=id
        bird = Bird(sighting)
        # object comprised of form input with addition of user_id
    
        list_bird_dicts = []
        search_input=Bird.query.filter_by(common_name=bird.common_name).all()
        print(search_input)

        if search_input == []:
            bird.__dict__['annual']='annual'
            bird.__dict__['lifetime']='lifetime'
            db.session.add(bird)
            db.session.commit()

        # Checks to see if sighted bird already in annual list
        #   if not, adds to annual list
        a=''
        for x in search_input:
            bird_dict = x.__dict__
            list_bird_dicts.append(bird_dict)
                     
        for x in list_bird_dicts:
            if x['annual'] == 'annual':
                a = 'annual'
            else:
                a = 'missing'

        if a == 'missing':
            bird.__dict__['annual']='annual'

        # Checks to see if sighted bird already in lifetime list
        #   if not, adds to lifetime list
        b=''
        for y in list_bird_dicts:
            if y['lifetime'] == 'lifetime':
                b = 'lifetime'
            else:
                b = None

        if b == None:
            bird.__dict__['lifetime']='lifetime'           
        
        db.session.add(bird)
        db.session.commit()

        #Could make this more specific, indicating which of three lists this particular
            #bird has been added to.
        flash(f'{bird.common_name} has been added to your lists.', category = 'success')
                
        return redirect(url_for('api.postSighting'))
    else:
        return render_template('sighting.html', form=bform)


@api.route('/annual_list', methods=['GET', 'POST'])
# @token_required
def getAnnualList():
       
    galform = AnnualListForm()

    if request.method == 'POST':
        
        if current_user.is_authenticated:

            gal_search=galform.data
            
            print(f'this is current users id" {current_user.id}')
            print('this is gal_search', gal_search)
            for k , v in gal_search.items():
                if v == '':
                    which_list = k
            
            if which_list == 'annual':
                current_datetime = datetime.utcnow()
                current_year = current_datetime.strftime('%Y')
                search_results = Bird.query.filter_by(annual=which_list).filter_by(user_id=current_user.id).filter_by(date_year=current_year)
                
                #beginning of removing duplicates:
                ind_dict = {}
                list_dicts = []
                for x in search_results:
                    ind_dict = x.__dict__
                    list_dicts.append(ind_dict)
                #have list of dictionaries here, still containing duplicate birds
                existing_dicts = set()
                filtered_list = []
                for d in list_dicts:
                    #make sure don't have capitalization match issue here.
                    #Think I made sure all new birds added in title case
                    #so should be ok here.
                    # if problem here, need to fix in line 136 too
                    if d['common_name'] not in existing_dicts:
                        existing_dicts.add(d['common_name'])
                        filtered_list.append(d)


                
            elif which_list == 'lifetime':
                search_results = Bird.query.filter_by(lifetime=which_list).filter_by(user_id=current_user.id)
                #convert Bird query objects to list of dictionaries
                ind_dict = {}
                list_dicts = []
                for x in search_results:
                    ind_dict = x.__dict__
                    list_dicts.append(ind_dict)
                #Removing dictionaries containing bird dublicates
                existing_dicts = set()
                filtered_list = []
                for d in list_dicts:
                    if d['common_name'] not in existing_dicts:
                        existing_dicts.add(d['common_name'])
                        filtered_list.append(d)
                            
            return render_template('annual_list_results.html', form = filtered_list,header=which_list ) 

        else:
            flash('Please log in to use access your annual or lifetime lists.', 'info')
            return redirect(url_for('auth.login'))

    else:
      
        return render_template('annual_list.html', form=galform)



# ***does not yet throw error if user puts in bird, year, country or state that is not in database***

@api.route('/list_search', methods=['GET', 'POST'])
# @token_required
def internalSearch():
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

    else:
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
          
        eb_search=ebform.data
        eb_search_input=EBirdSearch(eb_search)


        if int(eb_search['days']) > 30:
            flash(f"You entered {eb_search['days']} days.  Please enter a number of days between 1 and 30.", category='danger')
            return redirect(url_for('api.eBirdSearchFunction'))
        
        # dictionary of state codes
        state_code = get_regions('bdhdkslf0ktt', 'subnational1', 'US')
 
        #Gets eBird state code for spelled out state entered in form:
        miss_state = []
        for y in state_code:
            if y['name'] == eb_search_input.state.title():
                country_state = y['code']
                # above = "US-NY" if New york put into form
                miss_state.append(country_state)

        #Error Handling:  check for mispelled state:
        if miss_state == []:
            flash('Valid STATE name was not entered.  Please check spelling, and try again', category='danger')
            return redirect(url_for('api.eBirdSearchFunction'))

        #Gets eBird County code:
        county_code = get_regions('bdhdkslf0ktt', 'subnational2', f'{country_state}')

        miss_county = []
        for x in county_code:
            if x['name'] == eb_search_input.county.title():
                country_state_county = x['code']
                miss_county.append(country_state_county)
        if miss_county == []:
            flash('Valid COUNTY name was not entered.  Please check spelling, and try again', category='danger')
            return redirect(url_for('api.eBirdSearchFunction'))

        try:
            records = get_observations('bdhdkslf0ktt', f'{country_state_county}', back=f"{eb_search_input.days}")
            
            if records == []:
                flash('No sightings were reported during timeframe requested. Try increasing number of days.', category='danger')
                return redirect(url_for('api.eBirdSearchFunction'))

            return render_template('ebird_search_results.html', form = records, form_state=eb_search_input.state, form_county=eb_search_input.county, form_days=eb_search_input.days)
        
        except:
                #Error handling: '0' entered for days
                flash('Please enter a number of days from 1-30.', category='danger')
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

@api.route('/react', methods=['GET'])
def getBirds():
    birds = {'Birds': [a.to_dict() for a in React.query.all()]}
    return jsonify(birds), 200
    

@api.route('/other-user-search', methods=['GET', 'POST'])
# @token_required
def otherUserSearch():
    '''Searches data of other Bird Brain users'''
    #***<Need to add POST route here?***

    return render_template('other-user-search.html')

### Need to finish CRUD operations by creating UPDATE and DELETE functions based on below###

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
