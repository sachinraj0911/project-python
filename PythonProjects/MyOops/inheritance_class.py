class Student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno


class Marks:
        def __init__(self,m1,m2,m3):
            self.m1 = m1
            self.m2 = m2
            self.m3 = m3
            self.total = 0
            self.average = 0

        def __str__(self):
            return "{},{}".format(self.m1, self.m2, self.m3)

        def __add__(self, other):
            m1 = self.m1 + other.m1
            m2 = self.m2 + other.m2
            m3 = self.m3 + other.m3
            return (m1, m2, m3)


class Details(Student, Marks):
    def __init__(self, name, age, rollno, m1, m2, m3):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        Student.__init__(self, name, age, rollno)
        Marks.__init__(self, m1, m2, m3)

    def display2(self):
        self.total = self.m1 + self.m2 + self.m3
        print("Total:", self.total)

    def average1(self):
        self.average = (self.total / 3)
        print(self.average)

    def grade(self):
        if int(self.average) >= 70:
            print("Grade: A")
        elif 70 > int(self.average) >= 60:
            print("Grade: B")
        else:
            print("Grade: C")

    def display3(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Rollno:", self.rollno)


obj3 = Details('sachin', 21, 44, 80, 81, 82)
obj3.display3()  # output of name,age,rollno
obj3.display2()  # total
obj3.grade()
obj3.average1()