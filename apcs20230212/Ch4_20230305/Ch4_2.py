max = int(input('輸入Fibonacci Sequence範圍:'))

num1, num2 = 1, 1
print(num1, num2, sep=', ', end='')
next = num1+ num2
while(next<max):
    print(', %d' %next, end='')
    num1 = num2
    num2 = next
    next = num1+num2
