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
    ''' 取得指定節點 '''
    def getNode(self, index):
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        for i in range(index):          # 迴圈逐一查詢節點
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
            if(ptr==None):              # 下一個節點為None時提前終止迴圈
                break
        return ptr                      # 傳回第index個節點

import random
link = Linked_list()
for i in range(5):
    link.add(random.randint(1,100))

link.print_list()                   
#i = random.randint(0,4)
for i in range(5):
    print('索引%d:%d' %(i, 
      link.getNode(i).data))
