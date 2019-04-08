def czyliczbapierwsza(a):
    # a=12
    niepierwsza=0
    # for i in range(2,a):
    #     reszta=a%i
    #     # print (reszta)
    #     if reszta==0:
    #         # print (f'{a} to nie jest liczba pierwsza')
    #         return False
    #     # else:
    #         # print (f'{a} to jest liczba pierwsza')
    #
    # return True
    i=2
    while i<a :
        reszta=a%i
        if reszta == 0:
            return False
        i=i+1
    return True

liczba = 127
czy_pierwsza = czyliczbapierwsza(liczba)
if czy_pierwsza:
    print (f'podana liczba {liczba} jest pierwsza')
else:
    print (f'podana liczba {liczba} nie jest pierwsza')