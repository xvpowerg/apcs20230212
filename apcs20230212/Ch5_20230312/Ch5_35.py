class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
pt1 = Point(1,3)            
print(pt1)
