from os.path import join
import operator
from operator import itemgetter, attrgetter

dir = 'tempdata'
bname = join(dir, 'ssa-babynames-nationwide-2014.txt')

unordered = []
namesdict = {}

with open(bname) as x:
	for line in x:
		name, sex, babies = line.strip().split(',')
		if namesdict.get(name):
			namesdict[name] += int(babies)
		else:
			namesdict[name] = int(babies)

i = 1

for name in namesdict:
	if namesdict[name] >= 2000:
		unordered.append([name, namesdict[name], len(name)])

ordered = sorted(unordered, key=operator.itemgetter(2, 1), reverse=True)

for x in range(10):
	ip = str(i) + '.'
	print(ordered[x][0].ljust(11), str(ordered[x][1]).rjust(13), sep=' ')
	i += 1
