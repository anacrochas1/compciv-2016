import requests
import os

if not os.path.exists("tempdata"):
	os.makedirs("tempdata")

# # first file

if not os.path.exists("tempdata/googlemaps"):
	os.makedirs("tempdata/googlemaps")

link1url = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
resp = requests.get(link1url)
link1name = "tempdata/googlemaps/stanford.json"
zfile = open(link1name, 'wb')
zfile.write(resp.content)
zfile.close()

# # second file

if not os.path.exists("tempdata/mapzen"):
	os.makedirs("tempdata/mapzen")

link2url = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
resp = requests.get(link2url)

link2name = "tempdata/mapzen/stanford.json"
zfile = open(link2name, 'wb')
zfile.write(resp.content)
zfile.close()

# # number of lines and characters

fname = os.path.join('tempdata', 'googlemaps', 'stanford.json')
link1 = open(fname, 'r')

line_num1 = 0
for x in link1:
    line_num1 += 1
link1.close()

fname = os.path.join('tempdata', 'googlemaps', 'stanford.json')
link1 = open(fname, 'r')
googlemaps = link1.read()
len(googlemaps)

link1.close()

fname = os.path.join('tempdata', 'mapzen', 'stanford.json')
link2 = open(fname, 'r')
line_num = 0
for x in link2:
    line_num += 1
link1.close()

fname = os.path.join('tempdata', 'mapzen', 'stanford.json')
link1 = open(fname, 'r')
mapzen = link1.read()
len(mapzen)

link1.close()

# # Output

print("---")
print("Downloading from:", link1url)
print("Writing to:", link1name)
print("Wrote", line_num1, "lines and", len(googlemaps), "characters")
print("---")
print("Downloading from:", link2url)
print("Writing to:", link2name)
print("Wrote", line_num, "lines and", len(mapzen), "characters")
