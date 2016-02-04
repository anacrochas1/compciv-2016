from os.path import join
dir = 'tempdata'
bname = join(dir, 'ssa-babynames-nationwide-2014.txt')

flist = []
mlist = []

with open(bname) as x:
	for line in x:
		name, sex, babies = line.strip().split(',')
		babies = int(babies)
		if sex == 'F':
			flist.append((name, babies))
		elif sex == 'M':
			mlist.append((name, babies))

i = 1
print('Top baby girl names')
for thing in flist[:5]:
	ip = str(i) + '.'
	print(ip, thing[0], thing[1])
	i += 1

i = 1
print('\nTop baby boy names')
for thing in mlist[:5]:
	ip = str(i) + '.'
	print(ip, thing[0], thing[1])
	i += 1
