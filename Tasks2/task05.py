# Импортируйте все нужные библиотеки.
import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

PEP_URL = 'https://peps.python.org/numerical/'
Base = declarative_base()

class Pep(Base):
    __tablename__ = 'pep'
    id = Column(Integer, primary_key=True)
    type_status = Column(String(2))
    number = Column(Integer, unique=True)
    title = Column(String(200))
    authors = Column(String(200))

engine = create_engine('sqlite:///sqlite.db')
Base.metadata.create_all(engine)

request_session = requests.Session()
soup = BeautifulSoup(request_session.get(PEP_URL).text, features='lxml')
print(soup)


# Ваш код - здесь:
# создайте таблицу в БД;
# загрузите страницу PEP_URL;
# создайте объект BeautifulSoup;
# спарсите таблицу построчно и запишите данные в БД.