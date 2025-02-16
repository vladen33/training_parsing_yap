from bs4 import BeautifulSoup

if __name__ == '__main__':
    # simple_html = '<html><body><p>Это простой текст!<p></body></html>'
    # soup = BeautifulSoup(simple_html, features='html.parser')


    # В HTML-коде не закрыт парный тег <p>.
    simple_html = '<p>Закройте меня кто-нибудь!'
    # Подставьте в одинарные кавычки разные features —
    # сначала html.parser, а потом lxml.
    soup1 = BeautifulSoup(simple_html, features='html.parser')
    print('soup1 = ', soup1)
    print('=' * 50)
    soup2 = BeautifulSoup(simple_html, features='lxml')
    print('soup2 = ', soup2)
