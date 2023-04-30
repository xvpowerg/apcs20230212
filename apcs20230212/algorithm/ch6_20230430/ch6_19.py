class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items=[]
        self.weight=0
        self.value=0    
    def put(self, item):
        if self.weight+item.weight>capacity:
            return False
        else:
            self.items.append(item)
            self.weight += item.weight
            self.value += item.value
            return True
    def print(self):
        print('[', end='')
        for item in self.items:
            print(item, end=' ')
        print(']:', self.value)

class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.unitValue = self.value/self.weight
    def __lt__(self, other): 
        return self.unitValue < other.unitValue
    def __str__(self):
        return '(%d,%d)'%(self.weight, self.value)

weights = [1,2,3]
values = [20,60,45]
capacity = 5

knapsack = Knapsack(capacity)
items = []
for w,v in zip(weights, values):
    items.append(item(w,v))
sortedItems = sorted(items, reverse=True)
for i in sortedItems:
    if not knapsack.put(i):
        break
knapsack.print()
