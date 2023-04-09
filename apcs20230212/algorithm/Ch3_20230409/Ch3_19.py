class Node:                                     #堆疊鏈結節點的宣告
    def __init__(self, data):
        self.data=data                          #堆疊資料的宣告
        self.next=None                          #堆疊中用來指向下一個節點

class StackLL:
    def __init__(self):
        self.top=None
    def isEmpty(self):
        if(self.top==None):
            return True
        else:
            return False
    def push(self, item):  
        newNode = Node(item)
        newNode.next = self.top                 #將新節點指向堆疊的頂端
        self.top = newNode                      #新節點成為堆疊的頂端
    def pop(self):
        if self.isEmpty():
            print('堆疊為空!')
            return None
        else:
            ptr = self.top                      #指向堆疊的頂端
            self.top = self.top.next            #將堆疊頂端的指標指向下一個節點
            return ptr.data                     #將從堆疊取出的資料回傳給主程式
    def size(self):
        ptr = self.top
        count=0
        while ptr:
            ptr=ptr.next
            count+=1
        return count

stack = StackLL()
fruits = ['Apple', 'Banana', 'Cherry', 'Mango']
for fruit in fruits:
    stack.push(fruit)
    print('將 %s 水果堆入堆疊' % fruit)

print('堆疊有 %d 種水果' % stack.size())
while not stack.isEmpty():
    print(stack.pop())
