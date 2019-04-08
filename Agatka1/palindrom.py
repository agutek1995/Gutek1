def czypalindrom(slowo):
    literki=[]
    for i in slowo:
        literki.append(i)
    print (literki)
    for i in range(int((len(literki))/2)):
        if literki[i]==literki[-(i+1)]:
            pass
        else:

            return False
    return True

slowo = 'pajak'
wynik = czypalindrom(slowo)
if wynik:
    print (f'Slowo {slowo} jest palindromem')
else:
    print (f'Slowo {slowo} nie jest palindromem')
