import requests
import os

if not os.path.exists("tempdata"):
	os.makedirs("tempdata")

# # first file

if not os.path.exists("tempdata/ssa-babynames-nationwide-2014.txt"):
	os.makedirs("tempdata/ssa-babynames-nationwide-2014.txt")

burl = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(burl)
bname = "ssa-babynames-nationwide-2014.txt"
bfile = open(bname, 'wb')
bfile.write(resp.content)
bfile.close()


# # number of lines

bname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014.txt')
blink = open(bname, 'r')

line_num = 0
for x in blink:
    line_num += 1
blink.close()


# # Output

print("There are", line_num1, "lines in")


