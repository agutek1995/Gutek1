
# a = 5
#
# for i in range(3):
#     a = i
# print(a)

with open("data.txt", 'r') as file:
    lista3=[]

    for line in file:
        # print(line)
        # print(line.replace("jest", "nie jest"))
        lista3 = lista3 + line.split(" ")
    print (lista3)
    lista4=[]
    for i in lista3:
        lista4.append(i.rstrip())
    print (lista4)