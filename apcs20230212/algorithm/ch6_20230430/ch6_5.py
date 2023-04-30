class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None        
    def insert(self, data):
        ''' 建立二元樹 '''
        if self.data:                           # 如果根節點存在
            if data < self.data:                # 插入值小於目前節點值
                if self.left:
                    self.left.insert(data)      # 遞迴呼叫往下一層
                else:
                    self.left = Node(data)      # 建立新節點存放資料
            else:                               # 插入值大於目前節點值
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)                
        else:                                   # 如果根節點不存在
            self.data = data                    # 建立根節點
    def preorder(self):
        print(self.data, end='->')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()        
        print(self.data, end='->')
        if self.right:
            self.right.inorder()
    def search(self, val):
        ''' 搜尋特定值 '''                      
        if val < self.data:                     # 如果搜尋值小於目前節點值
            if not self.left:                   # 如果左子節點不存在
                return str(val) + " 不存在"
            return self.left.search(val)        # 遞迴繼續往左子樹找尋
        elif val > self.data:                   # 如果搜尋值大於目前節點值
            if not self.right:                  # 如果右子節點不存在
                return str(val) + " 不存在"
            return self.right.search(val)              
        else:
            return "找到 " + str(val)

bst = Node()  
datas = [20,15,17,30,32,4]
for d in datas:
    bst.insert(d)

n = eval(input("請輸入欲搜尋資料 : "))
print(bst.search(n))
