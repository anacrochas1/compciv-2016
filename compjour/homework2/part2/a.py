import requests
import pdfplumber
from os.path import basename
from glob import glob
import csv

urls = [
'http://www.edd.ca.gov/jobs_and_training/warn/WARNReportfor7-1-2014to06-30-2015.pdf', 
'http://www.edd.ca.gov/jobs_and_training/warn/WARN_Interim_041614_to_063014.pdf',
'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn14.pdf',
'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn13.pdf',
'http://www.edd.ca.gov/jobs_and_training/warn/eddwarncn12.pdf'
]

for url in urls:
	pdf_fname = 'CAWARN-' + basename(url)
	print("Downloading", url, 'into', pdf_fname)
	resp = requests.get(url)
	with open(pdf_fname, 'wb') as f:
		f.write(resp.content)

pdf_filenames = glob('CAWARN-*.pdf')
for pdf_fname in pdf_filenames:
	print("This is a filename of a pdf:", pdf_fname)
	pdf = pdfplumber.open(pdf_fname)
	type(pdf)

# PDF 1
pdf_fname = 'CAWARN-eddwarncn12.pdf'

outfile = open('CAWARN-eddwarncn12.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close


# PDF 2
pdf_fname = 'CAWARN-eddwarncn13.pdf'

outfile = open('CAWARN-eddwarncn13.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close


# PDF 3
pdf_fname = 'CAWARN-eddwarncn14.pdf'

outfile = open('CAWARN-eddwarncn14.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close


# PDF 4
pdf_fname = 'CAWARN-WARN_Interim_041614_to_063014.pdf'

outfile = open('CAWARN-WARN_Interim_041614_to_063014.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close

# PDF 5
pdf_fname = 'CAWARN-WARNReportfor7-1-2014to06-30-2015.pdf'

outfile = open('CAWARN-WARNReportfor7-1-2014to06-30-2015.csv', 'w')
outcsv = csv.writer(outfile)

pdf = pdfplumber.open(pdf_fname)
for page in pdf.pages:
    table = page.extract_table()
    for row in table[1:]:  # note how I'm still skipping the header
        outcsv.writerow(row)
outfile.close