for i in range(1,5+1):
    for j in range(1,3+1):
        for k in range(i):
            if i==1 :
                print(j*'*',end='')
            if i==2 :
                print(j*str(j)+(3-j)*' ',end='')
            if i==3 :
                print(j*chr(64+j)+(3-j)*' ',end='')
            if i==4 :
                print(j*str(k+1)+(3-j)*' ',end='')
            if i==5 :
                print('123'[0:j]+(3-j)*' ',end='')
        print()
