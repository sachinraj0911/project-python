class Employee:

    empcount = 0

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.empcount += 1

    def display_count(self):

        print("Total Employee:-->", Employee.empcount)

class Developer(Employee):
    def raise_in_salary(self):
        self.salary = int(self.salary * 1.20)


e1 = Developer("sachin", 26, 40000)
e2 = Developer("Raj", 25, 40000)
e3 = Developer("Machho", 36, 50000)
setattr(e1,"sex", "M")
print(getattr(e1,"name"))
print(e1.__dict__)

e3.display_count()