# In the future, Could use code below as model for providing birder users with info from ebird or endangered species api's;  need to make sure any additions to routes, etc. added too.

# import requests as r

# class Driver:
#     def __init__(self, apidict):
#         self.name = f"{apidict['Driver']['givenName']} {apidict['Driver']['familyName']}"
#         self.code = apidict['Driver']['code']
#         self.number = apidict['Driver']['permanentNumber']
#         self.points = apidict['points']
#         self.team = apidict['Constructors'][0]['name']
#         self.nationality = apidict['Driver']['nationality']
#         self.wins = apidict['wins']


# def getF1Drivers():
#     data = r.get('https://ergast.com/api/f1/current/driverStandings.json')
#     if data.status_code == 200:
#         data = data.json()
#     else:
#         return 'broken api'
#     seasonNum = data['MRData']['StandingsTable']['season']
#     api_list_of_standings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
#     driversList = {} # driver's 3 letter code as the key : Driver object as the value
#     for d in api_list_of_standings:
#         new_driver = Driver(d) # a different driver every step of the for loop
#         driversList[new_driver.code] = new_driver
#     # driversList = [Driver(x) for x in data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']]
#     print(driversList)
#     return {
#         'season': seasonNum,
#         'drivers': driversList
#     }