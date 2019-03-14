def znajdz_autora_i_zsumuj_go(nazwa_pliku, autor_do_sumowania):
    with open (nazwa_pliku, 'r') as file:
        lista=[]
        maxcena=0
        tytulmaxcena=''
        autorka=''
        suma=0
        for line in file:
            lista=line.split(';')
            cena=int(lista[2])
            maxcena=cena
            tytulmaxcena=lista[0]
            autorka=lista[1]

            if autor_do_sumowania==autorka:
                cenasumowana=cena
                suma=cenasumowana+suma

    print(f"Suma cen książek {autor_do_sumowania} wynosi {suma}")



znajdz_autora_i_zsumuj_go("books3.csv", "Lem")
znajdz_autora_i_zsumuj_go("books3.csv", "Brzechwa")
znajdz_autora_i_zsumuj_go("books3.csv", "Rowling")