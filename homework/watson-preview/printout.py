from os.path import join, basename
from glob import glob
import json
PICS_DIR = 'pics'
RECOG_DIR = 'responses'


HTML_FILENAME = 'printout.html'
htmlfile = open(HTML_FILENAME, 'w')
htmlfile.write("<html><title>Hello</title><body>")
htmlfile.write("<h1>Oie! This is Ana's awesome ibm watson analysis and I am your father.</h1>")

for jsonname in glob(join(RECOG_DIR, '*.json')):
    print("Extracting", jsonname)
    j = json.load(open(jsonname))
    img = j['images'][0]
    imgname = img['image']
    htmlfile.write("<h2>%s</h2>" % imgname)

    imgfilename = join(PICS_DIR, imgname)
    htmlfile.write('<img src="%s">' % imgfilename)

    htmlfile.write("<ol>")
    for i in range (len(j['images'][0]['scores'])):
    	name = j['images'][0]['scores'][i]['name']
    	score = str(j['images'][0]['scores'][i]['score'])
    	htmlfile.write('<li>%s -- %s</li>' % (name, score))
    htmlfile.write('</ol>')



htmlfile.close()