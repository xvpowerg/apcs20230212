a1 = int(input("首項"))
r =  int(input("公比"))
n =  int(input("項數"))

for i in range(n):
    print(a1 * r**i,end='\t')
print()    
    
def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n-1) * r
for i in range(1,n+1):
    print(getAn(i),end='\t')
print()    
