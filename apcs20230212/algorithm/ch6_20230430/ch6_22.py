class item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def getMaxValue(amt, itemList):
    dp = [0]*(amt + 1)
    dp[0] = 0
    for i in range(1, amt + 1):
        temp = [dp[i]]
        for item in itemList:
            if i>=item.weight:
                temp.append(item.value+dp[i-item.weight])
        dp[i] = max(temp)
    print(dp)
    return dp[-1]
      
weights = [1,2,3]
values = [20,60,45]
items = []
for w,v in zip(weights, values):
    items.append(item(w,v))

capacity = int(input('輸入背包載重量:'))
maxValue = getMaxValue(capacity, items)
print('%d公斤背包可放入物品最大價值為$%d' %(capacity, maxValue))
