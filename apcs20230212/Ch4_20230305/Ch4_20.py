def func(theList):
    print("func:",id(theList),theList)
    theList = [1,2,3,4]
    theList[0]= 80;
    print("func:",id(theList),theList)
    return
mylist = [10,20,30]
print("全域:",id(mylist),mylist)
func(mylist)
print("全域:",id(mylist),mylist)
