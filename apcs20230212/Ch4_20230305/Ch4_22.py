a = 5

def func():
    global a
    a+=2
    print("func: a = ",a)
    
print("全域:a=",a)
func()
print("全域:a=",a)
