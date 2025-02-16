import re

import requests_cache
from bs4 import BeautifulSoup

MAIN_DOC_URL = 'https://docs.python.org/3/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(MAIN_DOC_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    sidebar = soup.find('div', attrs={'class': 'sphinxsidebarwrapper'})
    ul_tags = sidebar.find_all('ul')

    for ul in ul_tags:
        if 'All versions' in ul.text:
            a_tags = ul.find_all('a')
            break
    else:
        raise Exception('Ничего не нашлось')

    results = []
    pattern = r'Python (?P<version>\d\.\d+) \((?P<status>.*)\)'
    for a_tag in a_tags:
        link = a_tag['href']
        text_match = re.search(pattern, a_tag.text)
        if text_match is None:
            version = a_tag.text
            status = ''
        else:
            version = text_match.group('version')
            status = text_match.group('status')
            results.append(
                (link, version, status)
            )

    # Печать результата.
    for row in results:
        print(*row)
