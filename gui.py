from tkinter import *
from narzedzia import *
from bazydanych import *

class Gui:

    def __init__(self, master):
        Baza.metadata.create_all(bind=plik)
        self.master = master

    def start(self):
        self.wyswietl_menu()
        self.master.mainloop()

    def wyczysc_ekran(self):
        for child in self.master.winfo_children():
            child.destroy()


    def dodaj_button(self, txt, com, r=None, c=None):
        butt = Button(self.master, text=txt, command=com)
        butt.grid(row=r, column=c)


    def dodaj_label(self, txt, r=None, c=None):
        lab = Label(self.master, text=txt)
        lab.grid(row=r, column=c)


    def wyswietl_menu(self):
        self.wyczysc_ekran()
        self.dodaj_button("Dodaj Film", self.menu_dodawania_filmu, 0, 0)
        self.dodaj_button("Wyświetl Filmy", self.wyswietlanie_filmow, 1, 0)
        self.dodaj_button("Dodaj Twórce", self.menu_dodawania_osob, 2, 0)
        self.dodaj_button("Wyświetl Twórców", self.wyswietlanie_tworcow, 3, 0)


    def wyswietlanie_filmow(self):
        self.wyczysc_ekran()
        filmy = session.query(Film).order_by(Film.tytul).all()
        self.dodaj_label("id", 0, 0)
        self.dodaj_label("tytul", 0, 1)
        self.dodaj_label("rok", 0, 2)
        self.dodaj_label("id rezysera", 0, 3)
        i = 1
        for film in filmy:
            self.dodaj_label(film.id, i, 0)
            self.dodaj_label(film.tytul, i, 1)
            self.dodaj_label(film.rok, i, 2)
            self.dodaj_label(film.rezyser, i, 3)
            i += 1
        self.dodaj_button("Powrot", self.wyswietl_menu)


    def menu_dodawania_osob(self):
        self.wyczysc_ekran()
        self.dodaj_label('Nazwisko:', 0)
        nazwisko = Entry(self.master)
        nazwisko.grid(row=0, column=1)
        self.dodaj_button("Dodaj", (lambda: self.dodawanie_osoby(nazwisko.get())))
        self.dodaj_button("Powrot", self.wyswietl_menu)

    def dodawanie_osoby(self, nazwisko):
        res = dodaj_osobe(nazwisko)
        self.dodaj_label(res)



    def menu_dodawania_filmu(self):
        self.wyczysc_ekran()
        self.dodaj_label('Tytuł:', 0, 0)
        tytul = Entry(self.master)
        tytul.grid(row=0, column=1)
        self.dodaj_label('Rok:', 1, 0)
        rok = Entry(self.master)
        rok.grid(row=1, column=1)


        osoby = [os.nazwisko for os in session.query(Osoby).order_by(Osoby.nazwisko).all()]

        self.dodaj_label('Rezyser:', 2, 0)
        rez = StringVar(self.master)
        rez.set(osoby[0])
        rezyser = OptionMenu(self.master, rez, *osoby)
        rezyser.grid(row=2, column=1)

        self.dodaj_button("Dodaj", (lambda: self.dodanie_filmu(tytul.get(), rok.get(), rez.get())))
        self.dodaj_button("Powrót", self.wyswietl_menu)

    def dodanie_filmu(self, tytul, rok, rezyser):
        dodaj_film(tytul, rok, rezyser)
        self.dodaj_label('Pomyslnie dodano film: '+ tytul)


    def wyswietlanie_tworcow(self):
        self.wyczysc_ekran()
        osoby = session.query(Osoby).order_by(Osoby.nazwisko).all()
        self.dodaj_label('id', 0, 0)
        self.dodaj_label('nazwisko', 0, 1)
        i = 1
        for os in osoby:
            self.dodaj_label(os.id, i, 0)
            self.dodaj_label(os.nazwisko, i, 1)
            i += 1
        self.dodaj_button("Powrót", self.wyswietl_menu)
