class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data                # 資料
        self.next = None                # 指標
class Circular_Linked_list():
    ''' 鏈結串列 '''
    def __init__(self): 
        self.head = None                # 鏈結串列第 1 個節點
    ''' 列印鏈結串列 '''
    def print_list(self):   
        ptr = self.head                 # 指標指向鏈結串列第 1 個節點
        print(ptr.data, end=' ')        # 列印第 1 個節點
        ptr = ptr.next                  # 移動指標到下一個節點
        while ptr!=self.head:
            print(ptr.data, end=' ')    # 列印節點
            ptr = ptr.next              # 移動指標到下一個節點
        print()
    ''' 取得指定節點 '''
    def getNode(self, index):
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        for i in range(index):          # 迴圈逐一查詢節點
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
            if(ptr==None):              # 下一個節點為None時提前終止迴圈
                break
        return ptr                      # 傳回第index個節點
    ''' 取得尾節點 '''
    def getLastNode(self):
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        while ptr.next!=self.head: 
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
        return ptr                      # 傳回第index個節點    
    ''' 新增頭節點 '''
    def add_front(self, item):
        lastNode = self.getLastNode()
        newNode = Node(item)
        newNode.next = self.head        # 將目前第一個節點設為新節點的下一個節點指標
        self.head = newNode             # 設定鏈結串列第一個節點為新節點
        lastNode.next = self.head
    ''' 新增尾節點 '''
    def add(self, item):
        newNode = Node(item)
        if self.head==None:
            self.head = newNode         # 設定鏈結串列第一個節點為傳入節點
            newNode.next = self.head
            return
        newNode.next = self.head
        lastNode = self.getLastNode()
        lastNode.next = newNode
    ''' 插入節點 '''
    def insert(self, index, item):
        newNode = Node(item)
        preNode = self.getNode(index-1)
        newNode.next = preNode.next
        preNode.next = newNode

import random
link = Circular_Linked_list()
for i in range(5):
    link.add(random.randint(1,100))
    link.print_list()

link.print_list()             
link.add_front(20)
link.print_list()                 
link.insert(3, 10)
link.print_list()
