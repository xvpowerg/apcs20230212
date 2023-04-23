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
        if self.gpa<student2.gpa:
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
print('插入排序法,原始資料為：', end='')
showdata(data)
n = len(data)

for i in range(1,n):
    tmp = data[i]
    for j in range(i):
        if data[j] < tmp:
            data.insert(j,tmp)
            del data[i+1]
            break
    showdata(data)


