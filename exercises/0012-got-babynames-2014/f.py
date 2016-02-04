from os.path import join
import string

dir = 'tempdata'
bname = join(dir, 'ssa-babynames-nationwide-2014.txt')

mydict = {}
for line in open(bname):
    name, sex, babies = line.strip().split(',')
    last_letter = name[-1]
    if mydict.get(last_letter):
        mydict[last_letter] += int(babies)
    else:
        mydict[last_letter] = int(babies)

for last_letter in string.ascii_lowercase:
	alph = mydict.get(last_letter)
	pnt = last_letter + '.'
	print(pnt, alph)
	