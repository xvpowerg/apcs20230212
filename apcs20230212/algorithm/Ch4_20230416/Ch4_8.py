from math import sqrt
while  True:
    n = int(input("請輸入整數-1離開"))
    if n == -1:
        break
    print(f"{n}=",end="")
    while True:
        for i in range(2,int(sqrt(n)) + 1):
            if n % i == 0:
                n = n // i
                if n == 1:
                    print(f"{i}\n",end="")
                else:
                    print(f"{i}*",end="")
                break
        else:
            print(n)
            break
