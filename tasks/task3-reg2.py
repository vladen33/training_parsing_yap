import re

from bs4 import BeautifulSoup

some_html = """
<article>
  Произвольный текст перемежается ссылками на разные картинки и документы.
  <a href="http://url.com/some_pic.jpg"><img src="..."></a>
  <a href="http://url.com/another_img.jpeg">Ссылка на картинку</a>
  <a href="http://url.com/not_an_image.docx">Документ Word</a>
  <a href="http://url.com/funny_pic.gif">Гифка</a>
  <a href="http://url.com/media1.png"><img src="..."></a>
  <a href="http://url.com/png_sheet.xlsx">Электронная таблица</a>
  <a href="http://url.com/it_s_a_trap.jpg.zip">Архив</a>
  <a href="http://url.com/pdf_with_gif.pdf">Документ PDF</a>
  <a href="http://url.com/something_strange.agif">Неизвестный объект</a>
</article>
"""
text = """
Найдите все теги <a>, содержащие ссылки на картинки, 
применяя поиск с использованием регулярных выражений. 
Картинками в данном задании считаются только те ссылки, 
которые заканчиваются на ".jpg", ".jpeg", ".gif" и ".png". 
Смотрите внимательно на ссылки, там много ловушек!
"""

soup = BeautifulSoup(some_html, 'lxml')
pictures = soup.find_all(attrs={'href': re.compile(r'.+\.(jpg|jpeg|gif|png)$')})
print(pictures)