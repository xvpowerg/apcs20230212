import math
def is_prime(num):
    # 要包含int(math.sqrt(num)) 算出的數字
    for i in range(2,int(math.sqrt(num)) + 1):
        if num  % i == 0:
            return False
        else:
            return True
n = int(input("請輸入整數"))
if is_prime(n):
    print("是質數")
else:
    print("不是質數")
