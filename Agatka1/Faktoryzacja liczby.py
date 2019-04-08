def czyliczbapierwsza(a):
    pierwsze=[]
    niepierwsze=[]
    for i in range(2,a):
        reszta=a%i
        if reszta==0:
            pierwsze.append(i)
            print(pierwsze)
    niepierwsze.append(i)
    print (niepierwsze)

            # return False

    return True

liczba = 30
czy_pierwsza = czyliczbapierwsza(liczba)
if czy_pierwsza:
    print (f'podana liczba {liczba} jest pierwsza')
else:
    print (f'podana liczba {liczba} nie jest pierwsza')
    rozklad=[]
    for i in range(2,a):
        reszta = a % i
        if reszta == 0:
            a=a/i
            rozklad.append(i)

