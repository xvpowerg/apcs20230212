class Stack():
    def __init__(self):
        self.my_stack = []
    def my_push(self,data):
        self.my_stack.append(data)
    def my_pop(self):
        return self.my_stack.pop()
    def size(self):
        return len(self.my_stack)
stack =  Stack()

stack.my_push("A")
stack.my_push("B")
stack.my_push("C")
stack.my_push("D")

for i in range(stack.size()):
    print(stack.my_pop())
