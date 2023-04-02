score1 =[[5,6,7],
         [11,12,13]]
print(score1[0][1])


print(len(score1))#R長度

print(len(score1[0]))#C長度

for i in range(len(score1)):
  for k in range(len(score1[i])):
    print(score1[i][k],end =" ")
  print()
  
print()

for a1 in score1:
    for a2 in a1:
        print(a2,end=" ")
    print()        
        
