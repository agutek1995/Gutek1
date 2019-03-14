with open ("liczby.txt", 'r') as file:
    suma=0
    for line in file:
        liczba=int(line)
        suma=suma+liczba
    print (suma)
