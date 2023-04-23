def sqrt_binary(x,min,max,pre=2):
    #當前上下限沒超過目前
    if ((max - min)<10**(-pre)):
          return (min+max)/2
    mid = (min+max)/2
    if (mid*mid < x):
        return sqrt_binary(x,mid,max,pre)
    else:
        return sqrt_binary(x,min,mid,pre)
            
num = int(input("輸入整數"))
print(f"{num}的平方根{sqrt_binary(num,0,num,3):.3f}")
