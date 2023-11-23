##1
colours1 = ["red", "blue"]
colours2 = colours1

colours2[1] = "green"

print(colours1)

#2
person1 = ["Swen", ["Seestrasse", "Konstanz"]]
person2 = person1.copy()
person2[0] = "Sarah"
print(person2)
print(person1)

person2[1][0] = "Bücklestraße"
print(person2) #['Sarah', ['Bücklestraße', 'Konstanz']]

print(person1) #['Swen', ['Bücklestraße', 'Konstanz']]