h = int(input("身高公分:"))
w = int(input("體重:"))
bmi = w / (((h/100))**2)
print(f"bmi:{bmi:.2f}")
# <18.5 輕
# 18.5~25 正常
# 25~30 過重
# >30 胖胖
if bmi <= 18.5:
   print("輕")
elif bmi  <= 25:
   print("正常")
elif bmi <= 30:
   print("過重")
else:
    print("胖胖")
 
