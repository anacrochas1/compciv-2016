from os.path import join
import csv
DATA_DIR = 'tempdata'
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled2014.csv')
rfile = open(WRANGLED_DATA_FILENAME, 'r')
datarows = list(csv.DictReader(rfile))
for r in datarows:
    r['total'] = int(r['total'])
    r['males'] = int(r['males'])
    r['females'] = int(r['females'])
    r['ratio'] = int(r['ratio'])
print("Popular names with a gender ratio bias of less than or equal to:")
bigdatarows = []
for row in datarows:
	if int(row['total']) >= 100:
		bigdatarows.append(row)
fxrows = [r for r in bigdatarows if r['ratio'] <= 60 ]
fbrows = [r for r in bigdatarows if r['ratio'] <= 70 ]
fcrows = [r for r in bigdatarows if r['ratio'] <= 80 ]
fdrows = [r for r in bigdatarows if r['ratio'] <= 90 ]
ferows = [r for r in bigdatarows if r['ratio'] <= 99 ]	
for row in fxrows[0:1]:
	print("60%:", (len(fxrows)), "/", (len((bigdatarows))))
for row in fbrows[0:1]:	
	print("70%:", (len(fbrows)), "/", (len((bigdatarows))))
for row in fcrows[0:1]:	
	print("80%:", (len(fcrows)), "/", (len((bigdatarows))))
for row in fdrows[0:1]:	
	print("90%:", (len(fdrows)), "/", (len((bigdatarows))))
for row in ferows[0:1]:	
	print("99%:", (len(ferows)), "/", (len((bigdatarows))))