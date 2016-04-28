import requests
import pdfplumber
from os.path import basename
from glob import glob
import csv

urls = [
'https://www.nccommerce.com/Portals/11/Documents/Reports/WARN/Warn.pdf', 
'https://www.nccommerce.com/Portals/11/Documents/Reports/WARN/warn-2015.pdf',
'https://www.nccommerce.com/Portals/11/WARN/Warn2014.pdf',
'https://www.nccommerce.com/Portals/11/WARN/Warn-2013.pdf'
]

for url in urls:
	pdf_fname = 'NCWARN-' + basename(url)
	print("Downloading", url, 'into', pdf_fname)
	resp = requests.get(url)
	with open(pdf_fname, 'wb') as f:
		f.write(resp.content)

pdf_filenames = glob('NCWARN-*.pdf')
for pdf_fname in pdf_filenames:
	print("This is a filename of a pdf:", pdf_fname)
	pdf = pdfplumber.open(pdf_fname)
	type(pdf)

# PDF 1
pdf_fname = 'NCWARN-Warn.pdf'

outfile = open('NCWARN-Warn.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close


# PDF 2
pdf_fname = 'NCWARN-warn-2015.pdf'

outfile = open('NCWARN-warn-2015.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close


# PDF 3
pdf_fname = 'NCWARN-Warn2014.pdf'

outfile = open('NCWARN-Warn2014.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close


# PDF 4
pdf_fname = 'NCWARN-Warn-2013.pdf'

outfile = open('NCWARN-Warn-2013.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close