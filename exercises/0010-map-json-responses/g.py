from os.path import join
import json
fname = join('tempdata', 'mapzen', 'stanford.json')
link2 = open(fname, 'r')
mapzen = json.loads(link2.read())
link2.close()

for result in mapzen['features']:
	metadata = result['properties']

	local = mapzen['features'][0]['properties']

	lb = str(metadata['label'])
	con = str(metadata['confidence'])
	lng = str(result['geometry']['coordinates'][0])
	lat = str(result['geometry']['coordinates'][1])

	print(';'.join([lb, con, lng, lat]))