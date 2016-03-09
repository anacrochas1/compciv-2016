from os.path import join, basename
START_YEAR = 1950
END_YEAR = 2015
DATA_DIR = 'tempdata'

for year in range(START_YEAR, END_YEAR, 5):
	names_dict = {}
	thefilename = join(DATA_DIR, 'yob' + str(year) + '.txt')
	thefile =  open(thefilename, 'r')
	for line in thefile:
		name, gender, count = line.split(',')
		if not names_dict.get(name): # need to initialize a new dict for the name
			names_dict[name] = {'M': 0, 'F': 0}
		names_dict[name][gender] += int(count)
	print(year)
	total_namecount = len(names_dict.keys())
	total_babycount = sum(v['F'] + v['M'] for v in names_dict.values())
	print("Total:", round(total_babycount / total_namecount), 'babies per name')
	# for boys and girls separately
	for gd in ['M', 'F']:
		babyct = 0
		namect = 0
		for v in names_dict.values():
			if v[gd] > 0:
				babyct += v[gd]
				namect += 1
		print("    %s:" % gd, round(babyct / namect), 'babies per name')




# at this point, we've read the entire file so we can close it
thefile.close()