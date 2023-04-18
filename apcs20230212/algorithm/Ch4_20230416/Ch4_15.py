def fact(n):
    result = 1
    for i in range(n,0,-1):
        result *= i
    return result

print("5!",fact(5))
