import requests_cache
from bs4 import BeautifulSoup

WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(WHATS_NEW_URL)
    response.encoding = 'utf-8'

    html_text = response.text

    soup = BeautifulSoup(response.text, features='lxml')

    res = soup.find(id="what-s-new-in-python")
    res2 = res.find_all('a')
    for r in res2:
        print(r)

    # links = [row['href'] for row in res2 if row.text.find("What’s New") >= 0]
    #
    # for link in links:
    #     print(link)
