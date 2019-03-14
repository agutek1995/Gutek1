# with open ("data.txt", "r") as file:
#     for line in file:
#         l=line.split(" ")
#         print (l)
#         print (", ".join(l))

with open("data.txt", "r") as file:
    lista11=[]
    for line in file:
        lista11=lista11+line.split()
    print (lista11)
    a =(lista11.count('jest'))
    print (f"Jest występuje {a}")
    for slowo in set(lista11):
        a = (lista11.count(slowo))
        print (slowo)
        print(f"występuje {a}")

# with open ("data2.txt","a") as file:
#     file.write("ala ma kota")


