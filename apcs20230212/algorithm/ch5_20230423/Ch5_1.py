from itertools import permutations

listo9=[1,2,3,4,5,6,7,8,9]
plist = list(permutations(listo9))

# list[4] - list[8] 個位數是6
# list[8] - list[4] 借位做減法後為6
# 313 - 137 借位後相減為6
for list in plist:
    if (list[0] == 6 or list[0] == 7):
        if ((list[4] - list[8] == 6) or (list[8] - list[4] == 4)):
            n1 = list[0] * 10000 + list[1]*1000 + list[2] * 100 + list[3] * 10 + list[4]
            n2 = list[5] * 1000 + list[6]*100 + list[7]*10 + list[8]
            if (n1-n2) == 66666:
                print(n1,"-",n2,"=66666")
