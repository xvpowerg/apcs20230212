a1,a2 = 1,3
print(a1,a2,sep="\t",end="\t")

for i in range(3,8):
   a3 = 3 * a2 - 2 * a1
   print(a3,end='\t')
   a1 = a2
   a2 = a3
print()

def seqFunc(x):
    if x == 1:
        return 1
    elif x == 2:
        return 3
    else:
        return 3 * seqFunc(x-1) -2*seqFunc(x-2)

for j in range(1,8):
    print(seqFunc(j),end='\t')
print()    
