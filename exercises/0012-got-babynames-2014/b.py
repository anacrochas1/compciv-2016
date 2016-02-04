from os.path import join
dir = 'tempdata'
bname = join(dir, 'ssa-babynames-nationwide-2014.txt')

babies = 0
with open(bname) as x:
	for line in x:
		babies += int(line.split(',')[2])

print ("There are", babies, "babies whose names were recorded in 2014.")