class Stack():
    def __init__(self, capacity):
        self.my_stack = [None]*capacity
        self.top = -1
        self.capacity = capacity
    def push(self, data):
        if self.isFull():
            print('堆疊已滿!')
        else:
            self.top+=1
            self.my_stack[self.top]=data
    def pop(self):
        if self.isEmpty():
            print('堆疊為空!')
            return None
        else:
            data = self.my_stack[self.top]
            self.my_stack[self.top] = None
            self.top-=1
            return data
    def size(self):
        return self.top+1
    def isEmpty(self):
        if(self.top==-1):
            return True
        else:
            return False
    def isFull(self):
        if(self.top>=self.capacity-1):
            return True
        else:
            return False

stack = Stack(3)
fruits = ['Apple', 'Banana', 'Cherry', 'Mango']
for fruit in fruits:
    print('將 %s 堆入堆疊' %fruit)
    stack.push(fruit)
print('堆疊有 %d 種水果' % stack.size())

for i in range(4):
    item = stack.pop()
    if (item):
        print('堆疊中取出%s' %item)
print('堆疊有 %d 種水果' % stack.size())
