import requests
import os

burl = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(burl)
bname = "tempdata/ssa-babynames-nationwide-2014.txt"

babies_list = []
lines = open(bname, 'r').readlines()
for x in lines:
    name, sex, babies = x.strip().split(',')
    row = [name, sex, int(babies)]
    babies_list.append(row)

def foo(x):
	return -x[2]

babies_list.sort(key = foo)

i = 1
for thing in babies_list[:10]:
	ip = str(i) + '.'
	print(ip, thing[0] +',', thing[1] +',', thing[2])
	i += 1