count = 0

for i in range(1,7):
    for j in range(1,7):
         if j <=  i:
             continue
         for k in range(1,7):
            if k <= j:
              continue
            for l in range(1,7):
                if l <= k:
                    continue
                count+=1
                print(f"{count} : {i},{j},{k},{l}")
                
   
'''
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                if i < j and j < k and k < l:
                    count+=1
                    print(f"{i},{j},{k},{l}")
'''                    
