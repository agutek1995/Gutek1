with open ("data.txt",'r') as file:
    slowa=[]
    for line in file:
        slowa=slowa+line.split(' ')
    print (slowa)
    czypodaneslowowystepuje='Jacek'
    if czypodaneslowowystepuje in slowa:
        print (f'Slowo {czypodaneslowowystepuje} jest w tekscie')
    else:
        print (f'Slowo {czypodaneslowowystepuje} nie wystepuje w tekscie')
    for i in slowa:
        iloscwystapien=slowa.count(i)
        jakieslowo=i
        print (f'Slowo {jakieslowo} wystepuje {iloscwystapien}')

