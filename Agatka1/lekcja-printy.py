# alfabet = "abcdefghijklmnopr"

# def pisaniea1(ilosc_a, literka):
#     for i in range(ilosc_a+1):
#         print( f"{alfabet[literka]}{alfabet[i]} ",end='')
#
# # pisaniea1(1, 4)
#
# def tabelka(wymiar):
#     for i in range(wymiar):
#         pisaniea1(wymiar,i)
#         print (' ')
# tabelka(16)
alfabet = "abcdefghijklmnopr"
alfabet2="ABCDEFGHIJKLMNOPRST"


def pisaniea1(ilosc_a, literka):
    for i in range(ilosc_a+1):
        print( f"{alfabet[literka]}{alfabet2[i]} ",end='')

# pisaniea1(1, 4)

def tabelka(wymiar):
    for i in range(wymiar):
        pisaniea1(wymiar,i)
        print (' ')
tabelka(16)