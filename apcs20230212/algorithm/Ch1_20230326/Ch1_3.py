for i in range(-4,5):
    for j in range(-4,5):
        if 4 - abs(j) > abs(i):
            print(" ",end="")
        else:
            print("*",end="")
    print()        
