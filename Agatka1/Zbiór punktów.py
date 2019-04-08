def najblizszepunkty(nazwa_pliku):
    with open (nazwa_pliku, 'r')as file:
        lista=[]
        wspolrzedne=''
        x=0
        y=0
        for line in file:
            lista=line.split(';')
            x=int(lista[1])
            y=int(lista[2])
            odleglosc

