class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None
n1 = Node(5)
n2 = Node(15)
n3 = Node(25)

lsp = n1
n1.next = n2
n2.next = n3

while lsp:
   print(lsp.data)
   lsp = lsp.next
   
