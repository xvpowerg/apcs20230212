list1 = [1,2,3,4,5]
def seq(x):
    return x **2

list2 = map(lambda x:x**2,list1)
print(list1)
print(list2)
print(list(list2))
