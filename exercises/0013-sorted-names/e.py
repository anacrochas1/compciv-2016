from os.path import join
import operator

dir = 'tempdata'
bname = join(dir, 'ssa-babynames-nationwide-2014.txt')

unordered = []
namesdict = {}

group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0

with open(bname) as x:
	for line in x:
		name, sex, babies = line.strip().split(',')
		if namesdict.get(name):
			namesdict[name] += int(babies)
		else:
			namesdict[name] = int(babies)

i = 1

for name in namesdict:
	unordered.append([name, namesdict[name]])

ordered = sorted(unordered, key=operator.itemgetter(1), reverse=True)

for x in range(len(ordered)):
	if x <= 9:
		group1 += ordered[x][1]
	elif x <= 99:
		group2 += ordered[x][1]
	elif x <= 999:
		group3 += ordered[x][1]
	elif x <= 9999:
		group4 += ordered[x][1]
	else:
		group5 += ordered[x][1]

i = 1

total = (group1 + group2 + group3 + group4 + group5)

print('Names 1 to 10:', (round((group1/total)*100,1)))
print('Names 11 to 100:', (round((group2/total)*100,1)))
print('Names 101 to 1000:', (round((group3/total)*100,1)))
print('Names 1001 to 10000:', (round((group4/total)*100,1)))
print('Names 10001 to 30579:', (round((group5/total)*100,1)))





