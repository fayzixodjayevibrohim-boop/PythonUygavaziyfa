import os
os.system("cls")

def chiqar(n):
    yigindi = 0
    for i in range(1, n + 1):
        print(i, end=" ")
        yigindi += i
    print("Yig'indi:", yigindi)

n = int(input())
chiqar(n)
