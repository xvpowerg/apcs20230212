class Employee:
    def __init__(self,name,salary = 20000):
        #print("__init__")
        self.name = name
        self.salary = salary
    def printInfo(self,title):
        print(title)
        print("name:",self.name)
        print("salary:",self.salary)
emp =Employee("Sean",50000)
#print(emp.name)
#print(emp.salary)
emp.printInfo("員工資訊1")
emp2 =Employee("Iris",25000)
emp2.printInfo("員工資訊2")
#print(emp2.name)
#print(emp2.salary)
