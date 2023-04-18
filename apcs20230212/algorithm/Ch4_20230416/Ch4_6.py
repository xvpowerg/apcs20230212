def primeList(number):
    primes = []
    for n in range(2,number+1):
        for i in primes:        
            if n % i == 0:
                break
        else:
            primes.append(n)
    return primes

n = 10
pList = primeList(n)
print(f"小於等於{n}的所有質數:",pList)

