class Node():
    ''' 節點 '''
    def __init__(self, data=None):
        self.data = data                # 資料
        self.next = None                # 指標

class Linked_list():
    ''' 建立鏈結串列 '''
    def __init__(self): 
        self.head = None                # 鏈結串列第一個節點
    ''' 列印鏈結串列 '''
    def print_list(self):   
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        while ptr:
            print(ptr.data)             # 列印節點
            ptr = ptr.next              # 移動指標到下一個節點    
    ''' 新增節點 '''
    def add(self, item):  
        newNode = Node(item)
        if self.head==None:
            self.head = newNode         # 設定鏈結串列第一個節點為傳入節點
            return
        ptr = self.head                 # 指標指向鏈結串列第一個節點
        while ptr.next: 
            ptr = ptr.next              # 指標指向鏈結串列下一個節點
        ptr.next = newNode              # 設定最後一個節點指標指向傳入節點
        
link = Linked_list()
data = [5, 15, 25]                      # 新增資料
for n in data:                          # 加入鏈結串列
    link.add(n)

link.print_list()                       # 列印鏈結串列 link
