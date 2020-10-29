from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sys import argv
from tkinter import *
from narzedzia import *

class Osoby(Baza):
    __tablename__ = "osoby"
    id = Column('id', Integer, primary_key=True)
    nazwisko = Column('nazwisko', String, unique=False)

class Film(Baza):
    __tablename__ = 'film'
    id = Column('id', Integer, primary_key=True)
    tytul = Column('tytul', String, unique=True)
    rok = Column('rok_produkcji', String(4))
    rezyser = Column('rezyser', ForeignKey('osoby.id'))
    operator = Column('operator', ForeignKey('osoby.id'))
    producent = Column('producent', ForeignKey('osoby.id'))
  
def dodaj_osobe(nazwisko):
    osoba = Osoby(nazwisko=nazwisko)
    session.add(osoba)
    session.commit()

def dodaj_film(tytul, rok, rezyser, operator, producent):
    rezyser_filmu = session.query(Osoby).filter_by(nazwisko=rezyser).first()
    operator_filmu = session.query(Osoby).filter_by(nazwisko=operator).first()
    producent_filmu = session.query(Osoby).filter_by(nazwisko=producent).first()
    film = Film(tytul=tytul,rok=rok, rezyser=rezyser_filmu.id, operator=operator_filmu.id, producent=producent_filmu.id)
    session.add(film)
    session.commit()

