from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
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


def dodaj_osobe(nazwisko):
    if nazwisko not in [os.nazwisko for os in session.query(Osoby).order_by(Osoby.nazwisko).all()]:
        osoba = Osoby(nazwisko=nazwisko)
        session.add(osoba)
        session.commit()
        return "Dodano pomyślnie twórce o nazwisku: " + nazwisko
    else:
        return "Ta osoba jest już w bazie: " + nazwisko



def dodaj_film(tytul, rok, rezyser):
    rezyser_filmu = session.query(Osoby).filter_by(nazwisko=rezyser).first()
    film = Film(tytul=tytul, rok=rok, rezyser=rezyser_filmu.id)
    session.add(film)
    session.commit()

