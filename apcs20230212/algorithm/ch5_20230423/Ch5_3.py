def combine(lst, n):
    #print(f"tag {tag} list:{lst} n:{n} for:{len(lst)-n}")
    out = []
    #當 m== n 或 n =1 時返回
    if len(lst)==n:#元素個數等於取值數量
        return [lst]
    elif n==1:#取值數量為1時傳回單一元素組成集合
        return [[x] for x in lst]
    else:        
        for i in range(len(lst)-n):#目前list數量減去取值數量
            for c1 in combine(lst[i+1:], n-1):#這是i索引屬值在裡面的狀況 C(n - 1, m - 1)
                ls = [lst[i]]#i索引屬值在裡面
                ls.extend(c1)
                if ls not in out:#排除重複部分
                    out.append(ls)
               
            for c2 in combine(lst[i+1:], n):#這是i索引屬值不在裡面的狀況 C(n - 1, m) 
                ls = []#i索引屬值不在裡面
                ls.extend(c2)
                if ls not in out:#排除重複部分
                    out.append(ls)                
    return out
myList = combine([1,2,3,4,5,6], 4)
for l in myList:
    print(l)
