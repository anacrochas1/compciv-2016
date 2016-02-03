from os.path import join
import json
fname = join('tempdata', 'googlemaps', 'stanford.json')
link1 = open(fname, 'r')
googlemaps = json.loads(link1.read())
link1.close()

for result in googlemaps['results']:
	address = result['formatted_address']

geo = googlemaps['results'][0]['geometry']['location']

lng = str(geo['lng'])
lat = str(geo['lat'])

print(';'.join([address, lat, lng]))