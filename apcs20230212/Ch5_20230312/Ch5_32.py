class Person:
   def __init__(self,name):
       self.name = name
   def sayHi(self):
       print("Hi!",self.name)
p1 = Person("Amy")
p1.sayHi()

mySayHi =  p1.sayHi

p1.sayHi()
Person.sayHi(p1)
mySayHi()
