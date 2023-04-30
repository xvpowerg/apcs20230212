class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
    def __lt__(self, other):
        return self.value<other.value
    def __str__(self):
        return '%d(%d)'%(self.weight,self.value)

def load(items, w):
    if not items:
        return 0
    if not w:
        return 0
    for i in range(len(items)):
        if items[i].weight>w:
            return 0
        elif items[i].weight == w:
            return items[i].value
        else:
            reItems = []
            reItems.extend(items[:i])
            reItems.extend(items[i+1:])
            return max(load(reItems, w),
                items[i].value+load(reItems, w-items[i].weight))

treasures = [50,160,20,100,20,60,90,120,150,30]
values = [40,10,50,60,50,20,50,30,60,30]
tItems = []
for w,v in zip(treasures, values):
    tItems.append(item(w,v))
tItems.sort(reverse=True)

capacity = int(input('輸入總載重量:'))
maxValue=load(tItems, capacity)
print('最多能載價值%d元的寶物'%maxValue)
