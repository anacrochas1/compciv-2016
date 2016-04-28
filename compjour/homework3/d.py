from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
from urllib.parse import urljoin
import re
import requests
RELIGION_WORDS = ['pray','holy spirit', 'God', 'Lord', 'Christ(?:ian\w*|mas)?', 'Islam', 'bless\w*'
                  'heaven', 'creator', 'Allah', 'M[uo]hammed', 'Jesus', 'Bible', 'Scriptures',
                  'Koran', 'shepherd']
RELIGION_REGEX = re.compile('(%s)' % '|'.join(RELIGION_WORDS), re.IGNORECASE)
# Note, the original URL is
# https://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html
# but Github mirror is faster
SOURCE_URL = 'http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_executed_offenders.html'


def extract_offender_name(soup):
    otag = soup.find('p', text=re.compile('Offender:'))
    offender_name = otag.find_next_sibling('p').text
    return offender_name

def extract_last_words(soup):
    otag = soup.find('p', text=re.compile('Last Statement:'))
    if not otag:
        otag = soup.find('span', text=re.compile('Last Statement:')).parent
    ptags = otag.find_next_siblings('p')
    return '\n'.join([p.text for p in ptags])


if __name__ == '__main__':
    inmates = {'religious': [], 'nonreligious': []}
    indexsoup = BeautifulSoup(requests.get(SOURCE_URL).text, 'lxml')
    for atag in indexsoup.find_all('a', text='Last Statement'):
        if 'no_last_statement.html' not in atag['href']:
            xurl = urljoin(SOURCE_URL, atag['href'])
            print('-------------------')
            print(Fore.WHITE + Style.BRIGHT + Back.BLACK + xurl + Style.RESET_ALL)

            xsoup = BeautifulSoup(requests.get(xurl).text, 'lxml')
            inmate_name = extract_offender_name(xsoup)
            inmate_words = extract_last_words(xsoup)
            print("Final words from:",
                   Fore.RED + Style.BRIGHT +  Back.YELLOW + inmate_name + Style.RESET_ALL, '\n')
            repl = Fore.WHITE + Style.BRIGHT + Back.BLUE + r'\1' + Style.RESET_ALL
            print(RELIGION_REGEX.sub(repl, inmate_words))

            r_words = RELIGION_REGEX.findall(inmate_words)
            if r_words:
                inmates['religious'].append(inmate_name)
            else:
                inmates['nonreligious'].append(inmate_name)

    print("==============================================================")
    print('Religious', len(inmates['religious']))
    print('Non-Religious', len(inmates['nonreligious']))