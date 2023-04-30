class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None
    def createTree(data):
        root = Node(data[0])
        for i in range(1, len(data)):
            newNode = Node(data[i])
            prev = ptr = root
            while ptr!=None:
                prev = ptr
                if data[i]<ptr.data:
                    ptr = ptr.left
                else:
                    ptr = ptr.right
            if data[i]<prev.data:
                prev.left = newNode
            else:
                prev.right = newNode
##            root.preorder()
##            print()
##            root.inorder()
##            print()
        return root
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

datas = [20,15,17,30,32,4]
bst = Node.createTree(datas)

bst.preorder()
print()
bst.inorder()
print()
