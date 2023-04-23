def showdata(data_list):
    for i in range(len(data_list)):
        print('%3d' %data_list[i],end='')
    print()

data=[16,25,39,63,27,12,8,45]	                # 原始資料 
print('氣泡排序法：原始資料為：')
showdata(data)

n = len(data)
print("========================")    
for i in range(1,n):
    for j in range(n-i):
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1],data[j]
    print(data)
print("========================")    
showdata(data)
