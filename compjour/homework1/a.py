import os
import requests
from csv import DictReader
os.makedirs('tempdata', exist_ok = True)


URL = 'http://stash.compjour.org/samples/stops-and-frisks/2012-nypd.csv'

TXT = requests.get(URL)

aname = 'tempdata/2012-nypd.csv'
afile = open(aname, 'w')
afile.write(TXT.text)
afile.close()

with open('tempdata/2012-nypd.csv', 'r') as f:
	datarows = list(DictReader(f))

i = 0
for row in datarows:
	if row['age'] == '17' and row['datestop'] == '6032012' and row['city'] == 'MANHATTAN' and row['crossst'] == 'MADISON AVENUE':
		i = i + 1
print(i)