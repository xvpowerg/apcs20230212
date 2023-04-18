from itertools import permutations,combinations
perm = permutations([1,2,3,4])
for i in list(perm):
    print(i)
print("===============")   
comb = combinations([1,2,3,4,5,6],3)
for i in list(comb):
    print(i)
