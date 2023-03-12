def getResult(s):
    if  60<=s<=100:
        return "及格"
    elif 0<= s < 60:
        return "不及格"
    else:
        raise OverflowError

score = int(input("輸入成績:"))
try:    
    print(getResult(score))
except:
    print("錯誤的成績!")
