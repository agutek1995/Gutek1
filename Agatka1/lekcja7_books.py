with open ("books.csv", 'r') as file:
    lista=[]
    maxcena=0
    tytulmaxcena=''
    autorka=''
    for line in file:
        lista=line.split(';')
        cena=int(lista[2])
        if cena> maxcena:
            maxcena=cena
            tytulmaxcena=lista[1]
            autorka=lista[0]

    print (f'Najdozsza ksiazka kosztujaca {maxcena} zlotych nosi tytul {autorka}  i napisala ja {tytulmaxcena}')