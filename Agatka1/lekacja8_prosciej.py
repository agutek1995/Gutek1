
class Book(object):

    def __init__(self, tytul: str, autor: str, cena: int):
        self.tytul = tytul
        self.autor = autor
        self.cena = cena

    def __repr__(self):
        return f"Książka {self.tytul}, autora: {self.autor}, cena: {self.cena}"

if __name__ == '__main__':

    cyberiada = Book("Cybieriada", "Lem", 20)
    lokomotywa=Book("Lokomotywa","Tuwim", 9)


    print(cyberiada.tytul)
    print(cyberiada.autor)
    print(cyberiada)
