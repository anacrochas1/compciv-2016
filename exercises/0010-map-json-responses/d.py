from os.path import join
import json
fname = join('tempdata', 'googlemaps', 'stanford.json')
link1 = open(fname, 'r')
googlemaps = json.loads(link1.read())
link1.close()

mydict = []

for x in googlemaps['results'][0]['address_components']:	
	mydict += [x['long_name']]

mydict = '; '.join(mydict)

print(mydict)