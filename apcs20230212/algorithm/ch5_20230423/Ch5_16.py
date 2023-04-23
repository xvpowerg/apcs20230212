import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()

def bin_search(data, val):
    low,high =0,len(data)-1
    mid = -1
    while not low > high:
        mid = (low + high) // 2
        print(mid)
        if val < data[mid]:
            high = mid - 1
        elif val > data[mid]:
            low = mid + 1
        else:
            return mid
    return -1

    low,high =0,len(data)-1
    mid = -1
    while not low > high:
        mid = (low + high) // 2
        print(mid)
        if va1 < data[mid]:
            high = mid - 1
        elif va1 > data[mid]:
            low = mid + 1
        else:
            return mid
    return -1

data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)

data.sort()
print('資料內容：')
showData(data)        

while True:
     val = int(input("輸入1~100 輸入-1結束:"))
     if val == -1:
         break
     pos = bin_search(data,val)

     if pos == -1:
         print("不存在")
     else:
         print(f"{val}的位置{pos+1}")
