from os.path import join, basename
from glob import glob
DATA_DIR = 'tempdata'

tally = {'M': set(), 'F': set()}

for fname in glob(join(DATA_DIR, '*.txt')):
    year = basename(fname)[3:7]
    if year >= "1950":
        for line in open(fname, 'r'):
            name, gender, babies = line.split(',')
            tally[gender].add(name)

print("F:  ", (len(tally['F'])), "M:  ", (len(tally['M'])))
print("F/M name ratio:  ", round((len(tally['F']))/(len(tally['M']))*100))

