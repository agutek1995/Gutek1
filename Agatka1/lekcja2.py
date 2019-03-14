lista=['tata', 'siostra']
print (lista)
lista.append('mama')
lista.append('mama')
print(lista.append('mama'))
lista.count('mama')
print (lista.count('mama'))
print (lista)
for i in lista:
    print (i)
# for j in enumerate(lista):
#     ind, txt = j
#     print (j)
lista.remove('tata')
print (lista)

lista2=['banan']
print(lista+lista2)
lista.extend(lista2)
print (lista)

lista3=['niebieski', 'czerwony']
lista=lista+lista3
lista+=lista3
print (lista)

if 'mama' in lista:
    print ('jest mama')

if 'pies' in lista:
    print ('jest pies')
else:
    print ('zgubilismy psa')

if 'kot' not in lista:
    print('brak kota')


