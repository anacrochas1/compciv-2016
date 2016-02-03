from os.path import join
import json
fname = join('tempdata', 'mapzen', 'stanford.json')
link1 = open(fname, 'r')
mapzen = json.loads(link1.read())
link1.close()

tp = mapzen['type']

metadata = mapzen['geocoding']['query']

txt = str(metadata['text'])
sz = str(metadata['size'])
bound = str(metadata['boundary.country'])

print('type:', tp)
print('text:', txt)
print('size:', sz)
print('boundary.country:', bound)