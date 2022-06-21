from ebird.api import get_region, get_adjacent_regions, get_regions, get_observations

records = get_observations('bdhdkslf0ktt', 'US-IN-053', back=14)

print(records)