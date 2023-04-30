treasures = [50, 160, 20, 100, 20, 60, 90, 120, 150, 30]
treasures.sort()
def load(items, w):
    if len(items)==0:
        return 0
    elif w==0:
        return 0
    else:
        for i in range(len(items)):
            if items[i]>w:
                return 0
            elif items[i] == w:
                return w
            else:
                #現在重量之前的 與 現在重量之後的 合併為一組陣列 剩下的其他重量
                reItems = items[:i]+items[i+1:]
                #現在重量 （item[i]）+ load （剩下的其他重量,扣除了目前重量的總重量) , 假如不放目前的重量
                return max(items[i]+load(reItems, w-items[i]),load(reItems, w))

amount = int(input('輸入總載重量:'))
answer=load(treasures, amount)
print('最多能載%d公斤寶物'%answer)
