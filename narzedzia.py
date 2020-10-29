from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Baza = declarative_base()
plik = create_engine('sqlite:///baza.db')
Baza.metadata.create_all(bind=plik)
Session = sessionmaker(bind=plik)
session = Session()

