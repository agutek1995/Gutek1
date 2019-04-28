def znajdz_x(x,n):
    for i in range(x):
        suma=(i**(2))+(n**(2))
        # print (f"{i}^2 + {n}^2 = {suma}", end="       ")
        if suma%17==0:
            print (f"Hura znalezione wartosci to {i}^2 + {n}^2 = {suma}")
# znajdz_x(3,3)

def znajdz_y(y):
    for i in range(y):
        # print (' ')
        znajdz_x(y,i)

znajdz_y(10)
#
# podzielnoscprzez5=znajdz_y(3)%5
# if podzielnoscprzez5==0:
#     print(podzielnoscprzez5)
