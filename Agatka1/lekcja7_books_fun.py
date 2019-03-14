def znajdz_max_cena(nazwa_pliku):
    with open (nazwa_pliku, 'r') as file:
        lista=[]
        maxcena=0
        tytulmaxcena=''
        autorka=''
        for line in file:
            lista=line.split(';')
            cena=int(lista[2])
            if cena> maxcena:
                maxcena=cena
                tytulmaxcena=lista[0]
                autorka=lista[1]
        return maxcena, tytulmaxcena, autorka


najdrozsza_cena, najdrozszy_tytul, najdrozsza_autorka = znajdz_max_cena("books.csv")
print (f'Najdozsza ksiazka kosztujaca {najdrozsza_cena} zlotych nosi tytul {najdrozszy_tytul}  i napisala ja {najdrozsza_autorka}')
print (f'W pliku books.csv najdrozsza ksiazka nosi tytuł {najdrozszy_tytul}')

najdrozsza_cena, najdrozszy_tytul, najdrozsza_autorka = znajdz_max_cena("books2.csv")
print (f'Najdozsza ksiazka kosztujaca {najdrozsza_cena} zlotych nosi tytul {najdrozszy_tytul}  i napisala ja {najdrozsza_autorka}')
print (f'W pliku books2.csv najdrozsza ksiazka nosi tytuł {najdrozszy_tytul}')