num = int(input('輸入整數:'))

print(num, '的因數:', end='')
for i in range(1, num+1):
    if(num%i!=0):
        continue
    print(i, end=' ')
