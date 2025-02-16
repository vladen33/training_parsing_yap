import requests
from bs4 import BeautifulSoup
from sqlalchemy import Column, Integer, String, create_engine, insert
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
peps = soup.select('#numerical-index table tbody')
pep_rows_soup = BeautifulSoup(str(peps), features='lxml' )
pep_rows = pep_rows_soup.find_all('tr')

db_session = Session(engine)

for pep in pep_rows:
    row = pep.text.split('\n')[:4]
    db_session.execute(insert(Pep).values(
        type_status = row[0],
        number = row[1],
        title = row[2],
        authors = row[3]
    ))
    db_session.commit()
