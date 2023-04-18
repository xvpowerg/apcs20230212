def fibr(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return  fibr(n - 1)+ fibr(n - 2)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    num1,num2 = 0,1
    nextNum = num1 + num2
    for i in range(2,n):
        num1 = num2
        num2 = nextNum
        nextNum = num1 + num2
    return  nextNum

print(fibr(8))
print(fib(8))
