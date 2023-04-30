treasures = [50,160,20,100,20,60,90,120,150,30]
treasures.sort()
shipLoad = []
total=0
capacity = 500
for treasure in treasures:
    if treasure+total<capacity:
        shipLoad.append(treasure)
        total+=treasure
    
print('總重量:%d公斤' %total)
print('船上共%d個寶物:'%len(shipLoad), shipLoad)
