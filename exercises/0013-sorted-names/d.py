from os.path import join

dir = 'tempdata'
bname = join(dir, 'ssa-babynames-nationwide-2014.txt')

f_list = []
m_list = []

with open(bname) as x:
	for line in x:
		name, sex, babies = line.strip().split(',')
		babies = int(babies)
		for letter in name:
			if letter == 'x':
				if sex == 'F':
					f_list.append((name, babies))
				elif sex == 'M':
					m_list.append((name, babies))
			elif letter == 'X':
				if sex == 'F':
					f_list.append((name, babies))
				elif sex == 'M':
					m_list.append((name, babies))
i = 1
print('Female')
for thing in f_list[:5]:
	ip = str(i) + '.'
	print(ip, (str(thing[0]).ljust(19)), thing[1])
	i += 1

i = 1
print('Male')
for thing in m_list[:5]:
	ip = str(i) + '.'
	print(ip, (str(thing[0]).ljust(19)), thing[1])
	i += 1
