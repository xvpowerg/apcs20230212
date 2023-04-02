scores=[87,66,90,65,70]
score_sum = 0
counts =  len(scores)
score_max = 0
score_min = 100
for i in range(counts):
 print(f"第{i+1}學生的成績{scores[i]}")
 myScore = scores[i]
 score_sum += myScore
 if myScore > score_max:
    score_max = myScore    
 if myScore < score_min:
     score_min = myScore

print("sum:",score_sum)
print(f"avg:{score_sum/counts:.2f}")
print("score_max:",score_max)
print("score_min:",score_min)     
     
    
