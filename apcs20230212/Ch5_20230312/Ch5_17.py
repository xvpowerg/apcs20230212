num1 = 10
num2  = 0
nums = [1,3,5,7,9]


try:
    print(num1/num2)
   
except ZeroDivisionError:        
    print("ZeroDivisionError:...")
finally:
    print("關閉資源!!")
