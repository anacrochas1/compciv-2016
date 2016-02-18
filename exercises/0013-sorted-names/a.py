import requests
import os

if not os.path.exists("tempdata"):
	os.makedirs("tempdata")

if not os.path.exists("0013-sorted-names/tempdata"):
	os.makedirs("0013-sorted-names/tempdata")

burl = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(burl)
bname = "tempdata/ssa-babynames-nationwide-2014.txt"
bfile = open(bname, 'wb')
bfile.write(resp.content)
bfile.close()


# # number of caracters

bname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
blink = open(bname, 'r')

count_letters = len(resp.text)
print("There are", count_letters, "characters in", bname)
