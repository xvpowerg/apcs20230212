class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data                # 資料
        self.next = None                # 向後指標
        self.prev = None                # 向前指標
class Double_linked_list():
    ''' 鏈結串列 '''
    def __init__(self): 
        self.head = None                # 鏈結串列頭部的節點
        self.tail = None                # 鏈結串列尾部的節點
    def getNode(self, index):
        ''' 取得指定節點 '''
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        for i in range(index):          # 迴圈逐一查詢節點
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
            if(ptr==None):              # 下一個節點為None時提前終止迴圈
                break
        return ptr                      # 傳回第index個節點
    def print_list_from_head(self):
        ''' 從頭部列印鏈結串列 '''   
        ptr = self.head                 # 指標指向鏈結串列第 1 個節點
        while ptr:
            print(ptr.data, end=', ')   # 列印節點
            ptr = ptr.next              # 移動指標到下一個節點
        print()
    def print_list_from_tail(self):
        ''' 從尾部列印鏈結串列 '''   
        ptr = self.tail                 # 指標指向鏈結串列尾部節點
        while ptr:
            print(ptr.data, end=', ')   # 列印節點
            ptr = ptr.prev              # 移動指標到前一個節點
        print()
    def append(self, new_node):
        ''' 將節點加入雙向鏈結串列 '''
        if isinstance(new_node, Node):      # 先確定這item是節點
            if self.head == None:           # 處理雙向鏈結串列是空的
                self.head = new_node        # 頭是new_node
                new_node.prev = None        # 指向前方
                new_node.next = None        # 指向後方
                self.tail = new_node        # 尾節點也是new_node
            else:                           # 處理雙向鏈結串列不是空的
                self.tail.next = new_node   # 尾節點指標指向new_node
                new_node.prev = self.tail   # 新節點前方指標指向前
                self.tail = new_node        # 新節點成為尾部節點
        return
    def delete(self, index):
        ''' 刪除指定節點 '''
        if(index==0):
            self.head=self.head.next
            self.head.prev = None
            return
        delNode = self.getNode(index)
        prevNode = delNode.prev
        prevNode.next = delNode.next
        if delNode.next == None:
            self.tail = prevNode
        else:
            nextNode = delNode.next
            nextNode.prev = delNode.prev
        return    

import random
link = Double_linked_list()
for i in range(6):
    link.append(Node(random.randint(1,100)))
    link.print_list_from_head()

i=random.randint(0,5)
link.delete(i)
print('刪除節點%d' %i)
link.print_list_from_head()
link.delete(4)
link.print_list_from_head()
link.delete(0)
link.print_list_from_head()
