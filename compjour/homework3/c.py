import requests
from os import makedirs
from os.path import join
URL_ENDPOINT = 'http://www.tdcj.state.tx.us/death_row/dr_executed_offenders'
INDEX_PAGES_DIR = 'index-texas'
makedirs(INDEX_PAGES_DIR, exist_ok=True)

for pagenum in INDEX_PAGES_DIR:
    resp = requests.get(URL_ENDPOINT, params={'page': pagenum})
    print("Downloaded", resp.url)

    fname = join(INDEX_PAGES_DIR, '{}.html'.format(pagenum))
    print("Saving to", fname)
    with open(fname, "w") as wf:
        wf.write(resp.text)