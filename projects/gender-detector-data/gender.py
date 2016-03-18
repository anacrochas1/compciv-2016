from os.path import join
import json
WRANGLED_DATA_FILENAME = join('tempdata', 'babynames', 'wrangledbabynames.json')

NAMES_DATA_ROWS = json.load(open(WRANGLED_DATA_FILENAME))

def detect_gender(name):
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        if name.lower() == row['name'].lower():
            result = row
            break
    return result