import os
os.system("cls")

def masala2(n):
    for i in range(n, 0, -1):
        if i % 2 == 0:
            print(i, end=" ")

masala2(10)