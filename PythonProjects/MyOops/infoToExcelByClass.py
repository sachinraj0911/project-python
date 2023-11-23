import csv
import os
class A:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

    def displayInfo(self):
        #print(self.fname,self.lname,self.age)
        csv_writer.writerow([self.fname, self.lname, self.age])


a1=A("sachin","kumar",28)
a2=A("sachin","kumar",28)
a3=A("sachinraj","kumar",28)

csv_file=open("info.csv",'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Fname','Lname','Age'])
#print("fname ""lname ""age")
a1.displayInfo()
a2.displayInfo()
a3.displayInfo()
