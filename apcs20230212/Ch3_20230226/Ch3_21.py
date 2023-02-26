num = int(input("輸入整數"))
if num % 2 == 0 and num % 3 == 0:
    print("是2也是3的倍數")
elif num % 2 == 0:
    print("是2的倍數")
elif num % 3 == 0:
    print("是3的倍數")
else:
    print("都不是")
    
