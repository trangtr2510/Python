#page21
#Tạo lớp Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def getArea(self):
        area = round(self.width * self.height,1)
        return area
    def getPerimeter(self):
        perimeter = round(2 * (self.width + self.height),1)
        return perimeter
    
#page26
#lay thuoc tinh width, height cua doi tuong rec1
r1 = Rectangle(10,5)
r2 = Rectangle(20,11)
x = r1.width
y = r1.height
print('Chieu rong: ', x)
print('Chieu dai: ', y)
#goi phuong thuc getArea, getPerimeter cua doi tuong rec1
dt = r1.getArea()
cv = r1.getPerimeter()
print('Dien tich: ', dt)
print('Chu vi: ', cv)
