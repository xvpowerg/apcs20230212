class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None        
    def insert(self, data):
        if self.data:  
            if data < self.data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)                
        else:
            self.data = data
    def preorder(self):
        print(self.data, end='->')
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def minNode(self):
        ptr = self
        while ptr.left:
            ptr = ptr.left
        return ptr
    def delete_r(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_r(val)
            else:
                print(val, '不存在')
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_r(val)
            else:
                print(val, '不存在')
        else:
            if not self.left:
                tmp = self.right
                self.data = None
                return tmp
            elif not self.right:
                tmp = self.left
                self.data = None
                return tmp
            else:             
                tmp = self.right.minNode()                
                self.data = tmp.data
                if self.right.data==tmp.data:
                    self.right=None
                else:
                    self.right.delete_r(tmp.data)
        return self            

bst = Node()  
datas = [20,15,17,30,32,27,4]
for d in datas:
    bst.insert(d)
bst.preorder()
print()
n = eval(input("請輸入欲刪除資料 : "))
bst.delete_r(n)
bst.preorder()
print()
