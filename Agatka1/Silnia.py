def silnia(a):
    wynik=1
    # a=4
    for i in range(1,a):
        wynik=wynik*(i+1)
    return wynik
print (f'Silnia z liczby 5 wynosi {silnia(5)}')
