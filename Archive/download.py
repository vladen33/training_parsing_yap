import re
from pathlib import Path
from urllib.parse import urljoin

import requests_cache
from bs4 import BeautifulSoup
BASE_DIR = Path(__file__).parent
DOWNLOADS_URL = 'https://docs.python.org/3/download.html'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, features='lxml')
    table_tag = soup.find('table', attrs={'class': 'docutils'})
    pdf_a4_tag = table_tag.find('a', attrs={'href': re.compile(r'.+pdf-a4\.zip$')})
    pdf_a4_link = pdf_a4_tag['href']
    archive_link = urljoin(DOWNLOADS_URL, pdf_a4_link)
    print(archive_link)
    filename = archive_link.split('/')[-1]
    downloads_dir = BASE_DIR / 'downloads'
    downloads_dir.mkdir(exist_ok=True)
    archive_path = downloads_dir / filename
    print(archive_path)
    response = session.get(archive_link)
    with open(archive_path, 'wb') as file:
        file.write(response.content)















