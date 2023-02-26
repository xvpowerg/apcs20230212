subjs = ["國文","數學","英文"]
scores = [100,80,95]
for i in range(len(subjs)):
    print(f"科目:{subjs[i]} 分數:{scores[i]}")

print(list(zip(subjs,scores)))
    
    
for n,s in zip(subjs,scores):
   print(f"科目:{n} 分數:{s}")
