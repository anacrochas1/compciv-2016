import csv
from os import makedirs
from os.path import join
from csv import DictReader, DictWriter
ORIGINAL_DATA_DIR = join('tempdata')
WRANGLED_DATA_DIR = join('tempdata', 'wrangled')

csvname = join(ORIGINAL_DATA_DIR,'rows.csv?accessType=DOWNLOAD')

wrangled_dir = join(WRANGLED_DATA_DIR)
wrangled_fname = join(WRANGLED_DATA_DIR, 'wrangledofficemayor.csv')
makedirs(wrangled_dir, exist_ok=True)

with open(csvname, 'r', encoding='windows-1252') as csvinput:
    print("Opening", csvname)
    reader = csv.reader(csvinput)
    header = next(reader) 

    with open(wrangled_fname, 'w') as csvoutput:
        print("Writing to", wrangled_fname)
        writer = csv.writer(csvoutput)
        writer.writerow(header)
        
        for row in reader:
            if 'OFFICE OF THE MAYOR' in row[1]:
                writer.writerow(row)