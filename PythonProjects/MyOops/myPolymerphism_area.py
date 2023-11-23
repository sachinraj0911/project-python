from math import pi as p


class Shape:
    length = int(input('enter the length :'))
    breadth = int(input('enter the breadth :'))
    radius = int(input('enter the radius :'))

    def area1(self):
        print(self.length,self.breadth,self.radius)


class Rect(Shape):
    def area1(self):
      self.area = self.length*self.breadth
      print('area of rectangle :',str(self.area))


class Circle(Shape):
    def area1(self):
        self.area= p*self.radius*self.radius
        print('area of circle is %0.2f'%(self.area))

obj1=Shape()
obj1.area1()
obj=Rect()
obj.area1()
obj2=Circle()
obj2.area1()