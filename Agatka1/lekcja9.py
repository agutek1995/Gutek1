from typing import List

from lekacja8_prosciej import Book

# lista= [1, 5, 3, 8, 6, 2, 3, 9, 12, 6, 3]
# naj=0
# for i in lista:
#     if i>naj:
#         naj=i
# print (naj)

lista_ksiazek: List[Book] = []
lista_ksiazek.append(Book("Cyberiada", "Lem", 18))
lista_ksiazek.append(Book("Pamiętnik znaleziony w wannie", "Lem", 26))
lista_ksiazek.append(Book("Harry Potter i kamień filozoficzny", "Rowling", 36))
lista_ksiazek.append(Book("Harry Potter i węzień askabanu", "Rowling", 12))
lista_ksiazek.append(Book("Szachy", "Szachowski", 6))

# print(lista_ksiazek)

suma=0
drogi=0
naj_autor=0
for i in lista_ksiazek:
    if i.autor=="Lem":
        suma=i.cena+suma
        slownik={i.}
    if i.autor=="Rowling":

    # if i.cena>drogi:
    #     naj_autor=i.autor
    #     drogi=i.cena
print (naj_autor)
