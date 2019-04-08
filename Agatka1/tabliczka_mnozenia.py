def wierszmnozenia(a,b):
    for i in range(a):
        mnozenie=i*b
        print(f"{i}*{b}={mnozenie:2}", end="      ")
# wierszmnozenia(4,2)

def tabliczkamnozenia(n):
    for i in range(n):
        print(' ')
        wierszmnozenia(n,i)

tabliczkamnozenia(5)
