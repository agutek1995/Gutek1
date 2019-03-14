from typing import List


class Book(object):

    def __init__(self, tytul: str, autor: str, cena: int):
        self.tytul = tytul
        self.autor = autor
        self.cena = cena

    def wypisz_autora(self):
        print(self.autor)

    def pobierz_cene_w_promocji(self):
        if self.autor == "Lem":
            return self.cena / 4
        return self.cena * 0.6

    def __repr__(self):
        return f"Książka {self.tytul}, autora: {self.autor}, cena: {self.cena}"

    def przywitaj_sie(self):
        return f"Dzień dobry, jestem Książka {self.tytul}, autora: {self.autor}, cena: {self.cena}"

def wczytaj_csv(plik_csv):
    ksiazki = []
    with open(plik_csv, 'r') as file:
        for line in file:
            lista = line.split(';')
            ksiazka = Book(lista[0], lista[1], int(lista[2]))
            ksiazki.append(ksiazka)
    return ksiazki

cyberiada = Book("Cybieriada", "Lem", 20)
lokomotywa=Book("Lokomotywa","Tuwim", 9)
lokomotywa.wypisz_autora()
print(cyberiada)
print(cyberiada.przywitaj_sie())
print(lokomotywa.przywitaj_sie())
wczytane_ksiazki: List[Book] = wczytaj_csv("books.csv")
print(wczytane_ksiazki)
wczytane_ksiazki.append(lokomotywa)
for k in wczytane_ksiazki:
    promocyjna_cena = k.pobierz_cene_w_promocji()
    print(f"książka: {k.tytul} w promocji kosztuje: {promocyjna_cena}")