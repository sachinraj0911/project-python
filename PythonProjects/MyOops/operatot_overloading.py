class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return "{},{}".format(self.x,self.y)

    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return (x,y)

    def __sub__(self, other):
        x=self.x-other.x
        y=self.y-other.y
        return (x, y)

a1=A(2,3)
a2=A(4,6)
print(a1+a2)
print(a1-a2)

