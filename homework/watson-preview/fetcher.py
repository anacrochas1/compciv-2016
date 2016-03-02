import requests
from os import makedirs
PICS_DIR = 'pics'
makedirs(PICS_DIR, exist_ok = True)
photos = ('a', 'b', 'c', 'd', 'e')
i = 0

URLS = ['http://images.nypl.org/index.php?id=5104173&t=w',
        'http://images.nypl.org/index.php?id=5104195&t=w',
        'http://images.nypl.org/index.php?id=1661023&t=w',
        'http://images.nypl.org/index.php?id=1661019&t=w',
        'http://images.nypl.org/index.php?id=1661010&t=w'
        ]

for url in URLS:
    print("Downloading", url)
    resp = requests.get(url)
    fname = 'pics/'+photos[i]+'.jpg'
    print("Saving to", fname)
    with open(fname, 'wb') as w:
        w.write(resp.content)
    i += 1