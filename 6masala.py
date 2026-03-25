import os
os.system("cls")

def masala6(son):
    while son > 0:
        raqam = son % 10    
        print(raqam, end=" ") 
        son = son // 10     
    print()


masala6(5678) 