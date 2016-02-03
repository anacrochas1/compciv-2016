
from os.path import join
import json
fname = join('tempdata', 'googlemaps', 'stanford.json')
link1 = open(fname, 'r')
googlemaps = json.loads(link1.read())
link1.close()

for result in googlemaps['results']:
	print(result['formatted_address'])