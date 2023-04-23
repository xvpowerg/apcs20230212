def showdata(data_list):
    for i in range(len(data_list)):
        print('%3d' %data_list[i],end='')
    print()

data=[16,25,39,63,27,12,8,45]
print('插入排序法：原始資料為：')
showdata(data)

n = len(data)

for i in range(1,n):
    tmp = data[i]
    for j in range(i):
        if data[j] > tmp:
            data.insert(j,tmp)
            del data[i+1]
            break
    showdata(data)
