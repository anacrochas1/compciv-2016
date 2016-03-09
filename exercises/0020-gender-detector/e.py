from os.path import join, basename
YEAR = 2014
DATA_DIR = 'tempdata'
nominhos = join(DATA_DIR, 'yob' +str(YEAR) + '.txt')

names_dict = {}
thenominhos = open(nominhos, 'r')
for line in thenominhos:
	name, gender, count = line.split(',')
	if not names_dict.get(name):
		names_dict[name] = {'M': 0, 'F': 0}
	names_dict[name][gender] += int(count)
thenominhos.close()

total_namecount = len(names_dict.keys())
total_babycount = 0
for v in names_dict.values():
	totes = v['M'] + v['F']
	total_babycount += totes
print("Total:", total_namecount, 'unique names for', total_babycount, 'babies')

ncount = 0
bcount = 0
for v in names_dict.values():
	if v['M'] > 0:
		bcount += v['M']
		ncount += 1
print("    M:", ncount, "unique names for", bcount, "babies")

ncount = 0
bcount = 0
for v in names_dict.values():
	if v['F'] > 0:
		bcount += v['F']
		ncount += 1
print("    F:", ncount, "unique names for", bcount, "babies")