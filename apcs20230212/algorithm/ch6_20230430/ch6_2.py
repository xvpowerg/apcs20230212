class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=' ')
        if self.right:
            self.right.inorder()

    def calc(self):
        if self.data==None:
            return 0
        elif self.data in ops:
            if self.data=='*' :
                return (self.left.calc() * self.right.calc())   #乘法回傳left * right
            elif self.data=='/' :
                return (self.left.calc() / self.right.calc())   #除法回傳left / right
            elif self.data=='+' :
                return (self.left.calc() + self.right.calc())   #加法請傳left + right
            elif self.data=='-' :
                return (self.left.calc() - self.right.calc())   #減法回傳left - right
        else:
            return self.data
        
ops = ['+','-','*','/']
n1 = Node('+')
n2 = Node('-'); n1.left = n2
n3 = Node('+'); n1.right= n3
n4 = Node('+'); n2.left = n4
n5 = Node(18);  n2.right= n5
n6 = Node('*'); n3.left = n6
n7 = Node('/'); n3.right= n7
n8 = Node(23);  n4.left = n8
n9 = Node('*'); n4.right= n9
n12= Node(2);   n6.left = n12
n13= Node(3);   n6.right= n13
n14= Node(8);   n7.left = n14
n15= Node(2);   n7.right= n15
n18= Node(12);  n9.left = n18
n19= Node(3);   n9.right= n19

n1.inorder()
print('=',n1.calc())
