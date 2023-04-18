def gcd(m,n):
    print(f"gcd({m},{n})",end=" ")
    if n == 0:
        return m
    else:        
        return gcd(n,m%n) 
print(gcd(20,14))
