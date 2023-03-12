class Employee:
    company = "巨匠電腦"
    phone = "02-223114537"
    def __init__(self,name):
        self.name = name
    def printInfo(self):
        print(self.name)
        print(Employee.company)
        print(Employee.phone)
emp1 = Employee("Sean")
emp2 = Employee("Vivin")
emp1.name = "Ken"
Employee.company = "好好玩電腦"
emp1.printInfo()
emp2.printInfo()
