from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'

for fname in glob(join(DATA_DIR, '*.txt')):
	tally = {'M': set(), 'F': set()}
	year = basename(fname)[3:7]
	if year >= "1950":
		for line in open(fname, 'r'):
			name, gender, babies = line.split(',')
			tally[gender].add(name)
		print(year)
		print("F:  ", (len(tally['F'])), "M:  ", (len(tally['M'])))
		print("F/M name ratio:  ", round(((len(tally['F']))/(len(tally['M']))*100)))
