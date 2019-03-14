
lista=list(range(10))
print (lista)
lista2=[]
for i in lista:
    lista2.append(i*10)
print (lista2)
print (lista)

lista3 = [i*10 for i in lista]
print (lista3)

lista4=[i+7 for i in lista]
print (lista4)
print([i+7 for i in lista])
print([7 for i in lista])
print([8 for i in lista])
print(["oko" for i in lista])
print([f"oko {i}" for i in lista])

for x in [f"oko {i}" for i in lista]:
    print(x*2)


# ['kotek 1', 'kotek 4', 'kotek 7']
print([f'kotek {3*i+1}' for i in [0,1,2]])



listal=['ciepłe', 'zimny', 'miękka']
listap=['mleko', 'lód', 'kanapa']
for i,j in zip(listal,listap):
    print(i,j)


zip(listal,listap)
print (list(zip(listal,listap)))



# para = "ona", "on"
# para = tuple("ona", "on")
# print(para)
# x, y = para
# print(x)
# print(y)
#
# for para in [('ciepłe', 'mleko'), ('zimny', 'lód'), ('miękka', 'kanapa')]:
#     print(para)
#     x, y = para
#     print(x)
#     print(y)
#
# for x, y in [('ciepłe', 'mleko'), ('zimny', 'lód'), ('miękka', 'kanapa')]:
#     print(x)
#     print(y)