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
    def add_front(self, item):  
        newNode = Node(item)
        newNode.next = self.head        # 將目前第一個節點設為新節點的下一個節點指標
        self.head = newNode             # 設定鏈結串列第一個節點為新節點

link = Linked_list()
data = [5, 15, 25]                      # 新增資料
for n in data:                          # 加入鏈結串列
    link.add_front(n)

link.print_list()                       # 列印鏈結串列 link
