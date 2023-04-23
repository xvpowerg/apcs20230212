btree = ['-']*2**3

print(len(btree))
btree[1]='A'
btree[2]='B'
btree[3]='C'
btree[5]='D'
btree[7]='E'

for i in range(1,len(btree)):
     if 2 * i + 1 < len(btree):
         print(btree[2*i],btree[2*i + 1])
     else:
         print()
