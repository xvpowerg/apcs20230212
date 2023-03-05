a = 5

def func():
    #a = 10
    #a += 2#會出錯
    a= 10
    a+=2
    print("func: a = ",a)
print("全域:a=",a)
func()
print("全域:a=",a)
