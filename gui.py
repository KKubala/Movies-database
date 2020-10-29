from tkinter import *
from narzedzia import *
from bazydanych import *

def wyczysc_ekran():
    for child in master.winfo_children():
        child.destroy()

def dodaj_button(txt, com, r=None, c=None):
    butt = Button(master, text=txt, command=com)
    butt.grid(row=r, column=c)

def dodaj_label(txt, r=None, c=None):
    lab = Label(master, text=txt)
    lab.grid(row=r, column=c)

def wyswietl_menu():
    wyczysc_ekran()
    dodaj_button("Dodaj Film", menu_dodawania_filmu, 0, 0)
    dodaj_button("Wyświetl Filmy", wyswietlanie_filmow, 1, 0)
    dodaj_button("Dodaj Twórce", menu_dodawania_osob, 2, 0)
    dodaj_button("Wyświetl Twórców", wyswietlanie_tworcow, 3, 0)

def wyswietlanie_filmow():
    wyczysc_ekran()
    filmy = session.query(Film).order_by(Film.tytul).all()
    dodaj_label("id", 0, 0)
    dodaj_label("tytul", 0, 1)
    dodaj_label("rok", 0, 2)
    dodaj_label("id rezysera", 0, 3)
    dodaj_label("id operatora", 0, 4)
    dodaj_label("id producenta", 0, 5)
    i = 1
    for film in filmy:
        dodaj_label(film.id, i, 0)
        dodaj_label(film.tytul, i, 1)
        dodaj_label(film.rok, i, 2)
        dodaj_label(film.rezyser, i, 3)
        dodaj_label(film.operator, i, 4)
        dodaj_label(film.producent, i, 5)
        i += 1
    dodaj_button("Powrot", wyswietl_menu)

def menu_dodawania_osob():
    wyczysc_ekran()
    dodaj_label('Nazwisko:', 0)
    nazwisko = Entry(master)
    nazwisko.grid(row=0, column=1)
    
    dodaj_button("Dodaj", (lambda: dodaj_osobe(nazwisko.get())))
    dodaj_button("Powrot", wyswietl_menu)

def menu_dodawania_filmu():
    wyczysc_ekran()
    dodaj_label('Tytuł:', 0, 0)
    tytul = Entry(master)  
    tytul.grid(row=0, column=1)
    dodaj_label('Rok:', 1, 0)
    rok = Entry(master)
    rok.grid(row=1, column=1)

    dodaj_label('Rezyser:', 2, 0)
    rezyser = Entry(master)  
    rezyser.grid(row=2, column=1)

    dodaj_label('Operator:', 3, 0)
    operator = Entry(master)  
    operator.grid(row=3, column=1)

    dodaj_label('Producent:', 4, 0)
    producent = Entry(master)  
    producent.grid(row=4, column=1)

    dodaj_button("Dadaj", (lambda: dodaj_film(tytul.get(), rok.get(), rezyser.get(), operator.get(), producent.get())))
    dodaj_button("Powrót", wyswietl_menu)

def wyswietlanie_tworcow():
    wyczysc_ekran()
    osoby = session.query(Osoby).order_by(Osoby.nazwisko).all()
    dodaj_label('id', 0, 0)
    dodaj_label('nazwisko', 0, 1)
    i = 1
    for os in osoby:
        dodaj_label(os.id, i, 0)
        dodaj_label(os.nazwisko, i, 1)
        i += 1
    dodaj_button("Powrót", wyswietl_menu)

master = Tk()
master.title("FilmwebNew")
master.geometry('400x400+100+100')

wyswietl_menu()
master.mainloop()