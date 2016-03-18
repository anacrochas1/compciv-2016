import requests
from os import makedirs
from os.path import join
from shutil import unpack_archive
SOURCE_URL = 'https://www.ssa.gov/oact/babynames/names.zip'
BABY_DATA_DIR = join('tempdata', 'babynames')
BABY_ZIP_PATH = join(BABY_DATA_DIR, 'names.zip')

makedirs(BABY_DATA_DIR, exist_ok=True)

print("Downloading", SOURCE_URL)
resp = requests.get(SOURCE_URL)

with open(BABY_ZIP_PATH, 'wb') as f:
    f.write(resp.content)

unpack_archive(BABY_ZIP_PATH, extract_dir=BABY_DATA_DIR)