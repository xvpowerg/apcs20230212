p = [[0]*5  for x in range(10)]#10 x 5的陣列
print(p)

for i in range(10):
    for k in range(5):
        p[i][k] = f"({i},{k})"

for a1 in p:
    for a2 in a1:
        print(a2,end=" ")
    print()    
