class Student:
    '''學生類別'''
    school="pcschool"
    count=0
    def __init__(self, name):
        self.name = name
        Student.count += 1
    def displayCount(self):
        """選示學生人數"""
        print("學生人數:  %d" % Student.count)
    def __printInfo__(self):
        return ("姓名: "+self.name)

print("類別所屬類別:", Student.__class__)
print("類別所屬模組:", Student.__module__)
print("類別名稱:", Student.__name__)
print("類別的父類別:", Student.__bases__)
print("類別空間字典:", Student.__dict__)
print("類別文件字串:", Student.__doc__)
print("方法文件字串:", Student.displayCount.__doc__)
print()

st = Student('Sean')
print("物件所屬類別:", st.__class__)
print("物件所屬模組:", st.__module__)
print("物件空間字典:", st.__dict__)
print("物件文件字串:", st.__doc__)
print("方法文件字串:", st.displayCount.__doc__)
