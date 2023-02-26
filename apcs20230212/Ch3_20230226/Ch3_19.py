score = 25

if score >= 60:
    print("及格")
    if score >= 90:
        print("上台領獎")
else:
    print("不及格")
    if score >= 40:
        print("補考")
    else:
        print("重修")
        
print("分數:",score)        
