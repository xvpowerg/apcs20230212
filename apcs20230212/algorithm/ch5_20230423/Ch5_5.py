from math import fabs
def sqrt_binary(x,pre=2):
    min,max=0,x
    while((max-min) > 10 ** (-pre)):#需扣除整數部分留下小數
        mid = (min+max) / 2       
        if (mid*mid > x):
            max = mid
        else:
            min = mid
        print(f"mid:{mid}")
    return mid

num = int(input("輸入整數"))
print(f"{num}的平方根{sqrt_binary(num,3):.3f}")
