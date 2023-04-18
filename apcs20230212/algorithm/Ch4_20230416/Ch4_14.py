def josephus(ls,skip):
    idx = skip - 1
    while len(ls) > 1:
        print(ls,end='\t')
        print(ls.pop(idx))
        #算下一次要刪除的idx
        idx = (idx + skip - 1) % len(ls)
    print(ls[0])

n = 12
m = 3
list1 = [*range(1,n+1)]

josephus(list1,m)
