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
    for a in a_tags:
        print(a)

