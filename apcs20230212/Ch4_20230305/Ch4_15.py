def dumFunc(n1,n2,*other):
    s = n1 + n2
    for i in other:
        s += i
    return s
print(dumFunc(1,2))
print(dumFunc(1,2,3,4,5))
print(dumFunc(1,2,3,4,5,6,7,8,9,10))
        
