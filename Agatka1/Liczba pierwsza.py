def czyliczbapierwsza(a):
    # a=12
    niepierwsza=0
    for i in range(2,a):
        reszta=a%i
        # print (reszta)
        if reszta==0:
            # print (f'{a} to nie jest liczba pierwsza')
            return False
        # else:
            # print (f'{a} to jest liczba pierwsza')

    return True

liczba = 2
czy_pierwsza = czyliczbapierwsza(liczba)
if czy_pierwsza:
    print (f'podana liczba {liczba} jest pierwsza')
else:
    print (f'podana liczba {liczba} nie jest pierwsza')