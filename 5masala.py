import os
os.system("cls")
def masala5():
  
    for i in range(10, 100):
        tub = True
        for j in range(2, i):
            if i % j == 0:
                tub = False
        if tub:
            print(i, end=" ")
    print()


masala5()  