from glob import glob
from os.path import join
BRIEFS_DIR = 'briefs'
filenames = glob(join(BRIEFS_DIR, '*.html'))

import re
for fname in filenames:
	with open(fname, 'r') as rf:
	    txt = rf.read()
	    txt = txt.upper()
	    if re.search(r'\bISIS\b', txt) or re.search(r'\bISIL\b', txt):
	        print(fname, "mentions ISIS/ISIL") 