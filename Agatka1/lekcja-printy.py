alfabet = "abcdefg"

def pisaniea1(ilosc_a, literka):
    for i in range(ilosc_a+1):
        print( f"{i}{literka} ",end='')

# pisaniea1(1, 4)

def tabelka(wymiar):
    for i in range(wymiar):
        pisaniea1(wymiar,i)
        print (' ')
tabelka(8)
