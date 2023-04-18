def gcd(m,n):
    while(n!=0):
        print(f"gcd({m},{n})",end=" ")
        r = m % n
        m = n
        n = r
    return m   
ans = gcd(20,14)
print(ans)
