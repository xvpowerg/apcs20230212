# 作業
s1 = 0
for i in range(7):
    s1 += 3+5*i
print('3+8+13+18+23+28+33 =', s1)

def serFunc1(x):
    if x == 1:
        return 3
    else:
        return serFunc1(x-1)+3+5*(x-1)#我知道目前的數是多少但不知道之前的是多少數值用遞迴算

print('3+8+13+18+23+28+33 =', serFunc1(7))

s2 = 0#首相是2公比是-2
for k in range(10):
    s2 += 2*(-2)**k
print('2-4+8-16+32-64+128-256+512-1024 =', s2)

def serFunc2(y):
    if y==1:
        return 2
    else:
        return serFunc2(y-1)-(-2)**y

print('2-4+8-16+32-64+128-256+512-1024 =', serFunc2(10))
