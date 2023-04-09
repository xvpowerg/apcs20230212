class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data                # 資料
        self.next = None                # 指標

class Linked_list():
    ''' 鏈結串列 '''
    def __init__(self): 
        self.head = None                # 鏈結串列第 1 個節點
    ''' 列印鏈結串列 '''
    def print_list(self):   
        ptr = self.head                 # 指標指向鏈結串列第 1 個節點
        while ptr:
            print(ptr.data, end=' ')             # 列印節點
            ptr = ptr.next              # 移動指標到下一個節點
        print()                         
    ''' 新增節點 '''
    def add(self, item):  
        newNode = Node(item)
        if self.head==None:
            self.head = newNode         # 設定鏈結串列第一個節點為傳入節點
            return
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        while ptr.next: 
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
        ptr.next = newNode
    ''' 取得指定物件索引 '''
    def indexOf(self, value):
        ptr = self.head
        i = 0
        while ptr:
            if(ptr.data==value):
                break
            ptr = ptr.next
            i += 1
        else:
            i=-i
        return i

import random
link = Linked_list()
for i in range(5):
    link.add(random.randint(1,10))

link.print_list()                       # 列印鏈結串列 link
target = random.randint(1,10)
i = link.indexOf(target)
if(i>=0):
    print('%d索引:%d' %(target, i))
else:
    print('%d不存在' %(target))                    # 列印鏈結串列 link
