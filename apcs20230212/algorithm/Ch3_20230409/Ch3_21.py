class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
    def __str__(self):
        if(self.next==None):
            return "{0}(None)".format(self.data)
        else:
            return "{0}({1})".format(self.data, self.next.data)
        
class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front==None
    def enqueue(self, data):
        newNode = Node(data)        
        if self.isEmpty():
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    def dequeue(self):
        if(self.isEmpty()):
            print("佇列為空!")
            return None
        else:
            item = self.front
            self.front = item.next
            if(self.front==None):
                self.rear = None
            return item
    def size(self):
        if(self.isEmpty()):
            return 0
        count=1
        ptr = self.front
        while ptr!=self.rear:
            ptr=ptr.next
            count+=1
        return count
    def print_list(self):   
        ptr = self.front
        while ptr:
            print(ptr, end='-')
            ptr = ptr.next
        print()

queue = Queue()
people = ['Amy', 'David', 'Sean', 'Nicole']
for person in people:
    queue.enqueue(person)
    print('將 %s 排入佇列' %person)
    #queue.print_list()
print('佇列中有%d個人' %queue.size())
for i in range(4):
    item = queue.dequeue()
    if(item):
        print('佇列中取出%s' %item.data)
        #queue.print_list()
print('佇列中有%d個人' %queue.size())
