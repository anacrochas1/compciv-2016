from os.path import join
dir = 'tempdata'
bname = join(dir, 'ssa-babynames-nationwide-2014.txt')

clark = emilia = 0

with open(bname) as x:
	for line in x:
		name, sex, babies = line.strip().split(',')
		if name == 'Daenerys':
			emilia += int(babies)
		elif 'Khalees' in name or 'Khaless' in name:
			clark += int(babies)

print('Daenerys:', emilia)
print('Khaleesi:', clark)