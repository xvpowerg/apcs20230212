class list_node:
    def __init__(self):
        self.val=0
        self.next=None

head=[list_node()]*9                            #宣告一個節點型態陣列

data=[[1,2],[2,1],[1,3],[3,1],                  #圖形邊線陣列宣告 
      [2,4],[4,2],[2,5],[5,2],
      [3,6],[6,3],[3,7],[7,3],
      [4,8],[8,4],[5,8],[8,5],
      [6,8],[8,6],[8,7],[7,8]]

for i in range(1,9):                            #共有八個頂點
    head[i]=list_node()                         #設定各個串列首的初值
    head[i].val = i
    head[i].next=None
    ptr=head[i]                                 #設定指標為串列首
    for j in range(len(data)):                  #二十條邊線
        if data[j][0]==i:                       #如果起點和串列首相等，則把頂點加入串列
            newnode=list_node()
            newnode.val=data[j][1]
            newnode.next=None
            while ptr.next:
                ptr=ptr.next            
            ptr.next=newnode                    #加入新節點

run=[0]*9
print('圖形的鄰接串列內容:')                    #列印圖形的鄰接串列內容            
for j in range(1,9):
    run[i]=0                                    #設定所有頂點成尚未走訪過
    print('頂點 %d =>' %head[j].val,end='')
    ptr=head[j] 
    while ptr.next:
        ptr=ptr.next
        print('[%d] ' %ptr.val,end='')
    print()
    
def bfs(current, queue):
    if run[current]==0:
        run[current]=1                          #將走訪過的頂點設定為1
        print('[%d]' %current,end='')
        ptr=head[current].next
        while ptr!=None:
            if run[ptr.val]==0 and \
               ptr.val not in queue:
                queue.append(ptr.val)
            ptr = ptr.next
    if not queue:
        return
    else:
        nextNode = queue.pop(0)
        bfs(nextNode, queue)

print('廣度優先走訪頂點：')                     #列印廣度優先走訪的頂點
queue = []
bfs(1,queue)
print()
