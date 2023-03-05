def func(theList):
    print("func:",id(theList),theList)
    theList[2] = "Hi"
    print("func:",id(theList),theList)
    return
mylist = [10,20,30]
print("全域:",id(mylist),mylist)
func(mylist)
print("全域:",id(mylist),mylist)
