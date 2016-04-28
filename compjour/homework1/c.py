import os
import requests
from csv import DictReader

os.makedirs('tempdata3', exist_ok = True)
url = 'http://stash.compjour.org/samples/stops-and-frisks/2014-nypd.csv'

TXT = requests.get(url)

aname = 'tempdata3/2014-nypd.csv'
afile = open(aname, 'w')
afile.write(TXT.text)
afile.close()

with open('tempdata3/2014-nypd.csv', 'r') as f:
	datarows = list(DictReader(f))

print(len(datarows))

a = 0
for row in datarows:
	if row['arstmade'] == 'N':
		a = a + 1
print("Number of completely innocent people is", (a))

print((a)/(len(datarows))*100)

b = 0
for row in datarows:
	if row['race'] == 'B':
		b = b + 1
print("Blacks are", (b))
print("Blacks equal", (b)/(len(datarows))*100)

c = 0
for row in datarows:
	if row['race'] == 'Q' or row['race'] == 'P':
		c = c + 1
print("Latinos are" , (c))
print("Latinos equal", (c)/(len(datarows))*100)


d = 0
for row in datarows:
	if row['race'] == 'W':
		d = d + 1
print("Whites are" , (d))
print("Whites equal", (d)/(len(datarows))*100)

