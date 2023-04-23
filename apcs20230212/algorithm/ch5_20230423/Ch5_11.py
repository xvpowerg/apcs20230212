def showdata(data_list):
    print('[', end='')
    for i in range(len(data_list)):
        print(data_list[i],end=' ')
    print(']')
    
class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
    def __lt__(self, student2):
        if self.age<student2.age:
            return True
        else:
            return False
    def __str__(self):
        return '%5s(%d,%.1f)'%(self.name,self.age,self.gpa)

data=[Student('Amy', 15, 4.2),
      Student('Bill', 16, 3.8),
      Student('Chris', 13, 4.0),
      Student('David', 19, 4.8),
      Student('Ed', 17, 2.6)]
print('選擇排序法:原始資料為：', end ='')
showdata(data)

n = len(data)

for i in range(n-1):
    minIdx = i
    for j in range(i+1, n):
        if(data[j]<data[minIdx]):
            minIdx = j
    data[i], data[minIdx] = data[minIdx], data[i]
    print('第 %d 次掃描後的結果是：' %(i+1), end ='')
    showdata(data)
	
print('選擇排序之後的資料為：', end =' ')
showdata(data)
