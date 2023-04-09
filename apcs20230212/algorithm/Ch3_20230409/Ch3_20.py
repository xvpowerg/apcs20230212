class Queue():
  def __init__(self):
      self.my_queue = []
  def enqueue(self,data):
      self.my_queue.append(data)
  def dequeue(self):
      return self.my_queue.pop(0)
  def size(self):
      return len(self.my_queue)
  def isEmpty(self):
      return len(self.my_queue) == 0

queue =   Queue()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.enqueue("D")

for i in range(queue.size()):
    print(queue.dequeue())
