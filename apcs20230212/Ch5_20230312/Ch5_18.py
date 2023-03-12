num1 = 10
num2  = 0
nums = [1,3,5,7,9]

try:
 #print(num1 / num2)
    print(nums[100])
    
except Exception as ex:
    print("type:",type(ex))
    print("msg:",str(ex))
finally:
    print("資源清理")
