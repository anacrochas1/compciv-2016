from os.path import join, basename
import json
BABY_DATA_DIR = join('tempdata', 'babynames')
WRANGLED_DATA_FILENAME = join(BABY_DATA_DIR, 'wrangledbabynames.json')
START_YEAR = 1950
END_YEAR = 2014

years = list(range(START_YEAR, END_YEAR, 10))

years.append(END_YEAR)

namesdict = {}
for year in years:
    filename = join(BABY_DATA_DIR, 'yob' + str(year) + '.txt')
    print("Parsing", filename)
    with open(filename, 'r') as thefile:
        for line in thefile:
            name, gender, count = line.split(',')
            if not namesdict.get(name):
                namesdict[name] = {'F': 0, 'M': 0}
            namesdict[name][gender] += int(count)

my_awesome_list = []

for name, babiescount in namesdict.items():
    xdict = {'name': name, 'females': babiescount['F'], 'males': babiescount['M']}
    xdict['total'] = xdict['males'] + xdict['females']
    if xdict['females'] >= xdict['males']:
        xdict['gender'] = 'F'
        xdict['ratio'] = round(100 * xdict['females'] / xdict['total'])
    else:
        xdict['gender'] = 'M'
        xdict['ratio'] = round(100 * xdict['males'] / xdict['total'])

    my_awesome_list.append(xdict)

with open(WRANGLED_DATA_FILENAME, 'w') as j:
    j.write(json.dumps(my_awesome_list, indent=2))