from os.path import join
dir = 'tempdata'
bname = join(dir, 'ssa-babynames-nationwide-2014.txt')

fname = mname = 0

with open(bname) as x:
	for line in x:
		name, sex, babies = line.strip().split(',')
		if sex == 'F':
			fname += int(babies)
		elif sex == 'M':
			mname += int(babies)

print('F:', fname)
print('M:', mname)