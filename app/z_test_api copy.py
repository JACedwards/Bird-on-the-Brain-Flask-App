from sre_constants import IN
from ebird.api import get_region, get_adjacent_regions, get_regions, get_observations

# county_code = [{'code': 'US-IN-001', 'name': 'Adams'}, {'code': 'US-IN-003', 'name': 'Allen'}, {'code': 'US-IN-005', 'name': 'Bartholomew'}, {'code': 'US-IN-007', 'name': 'Benton'}, {'code': 'US-IN-009', 'name': 'Blackford'}, {'code': 'US-IN-011', 'name': 'Boone'}, {'code': 'US-IN-013', 'name': 'Brown'}, {'code': 'US-IN-015', 'name': 'Carroll'}, {'code': 'US-IN-017', 'name': 'Cass'}, {'code': 'US-IN-019', 'name': 'Clark'}, {'code': 'US-IN-021', 'name': 'Clay'}, {'code': 'US-IN-023', 'name': 'Clinton'}, {'code': 'US-IN-025', 'name': 'Crawford'}, {'code': 'US-IN-027', 'name': 'Daviess'}, {'code': 'US-IN-033', 'name': 'DeKalb'}, {'code': 'US-IN-029', 'name': 'Dearborn'}, {'code': 'US-IN-031', 'name': 'Decatur'}, {'code': 'US-IN-035', 'name': 'Delaware'}, {'code': 'US-IN-037', 'name': 'Dubois'}, {'code': 'US-IN-039', 'name': 'Elkhart'}, {'code': 'US-IN-041', 'name': 'Fayette'}, {'code': 'US-IN-043', 'name': 'Floyd'}, {'code': 'US-IN-045', 'name': 'Fountain'}, {'code': 'US-IN-047', 'name': 'Franklin'}, {'code': 'US-IN-049', 'name': 'Fulton'}, {'code': 'US-IN-051', 'name': 'Gibson'}, {'code': 'US-IN-053', 'name': 'Grant'}, {'code': 'US-IN-055', 'name': 'Greene'}, {'code': 'US-IN-057', 'name': 'Hamilton'}, {'code': 'US-IN-059', 'name': 'Hancock'}, {'code': 'US-IN-061', 'name': 'Harrison'}, {'code': 'US-IN-063', 'name': 'Hendricks'}, {'code': 'US-IN-065', 'name': 'Henry'}, {'code': 'US-IN-067', 'name': 'Howard'}, {'code': 'US-IN-069', 'name': 'Huntington'}, {'code': 'US-IN-071', 'name': 'Jackson'}, {'code': 'US-IN-073', 'name': 'Jasper'}, {'code': 'US-IN-075', 'name': 'Jay'}, {'code': 'US-IN-077', 'name': 'Jefferson'}, {'code': 'US-IN-079', 'name': 'Jennings'}, {'code' : 'US-IN-135', 'name': 'Randolph'}, {'code': 'US-IN-137', 'name': 'Ripley'}, {'code': 'US-IN-139', 'name': 'Rush'}, {'code': 'US-IN-143', 'name': 'Scott'}, {'code': 'US-IN-145', 'name': 'Shelby'}, {'code': 'US-IN-147', 'name': 'Spencer'}, {'code': 'US-IN-141', 'name': 'St. Joseph'}, {'code': 'US-IN-149', 'name': 'Starke'}, {'code': 'US-IN-151', 'name': 'Steuben'}, {'code': 'US-IN-153', 'name': 'Sullivan'}, {'code': 'US-IN-155', 'name': 'Switzerland'}, {'code': 'US-IN-157', 'name': 'Tippecanoe'}, {'code': 'US-IN-159', 'name': 'Tipton'}, {'code': 'US-IN-161', 'name': 'Union'}, {'code': 'US-IN-163', 'name': 'Vanderburgh'}, {'code': 'US-IN-165', 'name': 'Vermillion'}, {'code': 'US-IN-167', 'name': 'Vigo'}, {'code': 'US-IN-169', 'name': 'Wabash'}, {'code': 'US-IN-171', 'name': 'Warren'}, {'code': 'US-IN-173', 'name': 'Warrick'}, {'code': 'US-IN-175', 'name': 'Washington'}, {'code': 'US-IN-177', 'name': 'Wayne'}, {'code': 'US-IN-179', 'name': 'Wells'}, {'code': 'US-IN-181', 'name': 'White'}, {'code': 'US-IN-183', 'name': 'Whitley'}]


def getCountyByDate(county_name, days):

    county_code = get_regions('bdhdkslf0ktt', 'subnational2', 'US-IN')

    # county_name = 'Grant'

    for x in county_code:
        if x['name'] == county_name:
            country_state_county = x['code']

    records = get_observations('bdhdkslf0ktt', f'{country_state_county}', back=f"{days}")
    return records

print(getCountyByDate('Grant', '14'))