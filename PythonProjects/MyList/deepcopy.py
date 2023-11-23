from copy import deepcopy
person1 = ["Swen", ["Seestrasse", "Konstanz"]]

person2 = deepcopy(person1) #copy it deeply and create a different object refrence for this.

print(id(person1[1]), id(person2[1]))

##person1[0] and person2[0]. They reference the same string
print(id(person1[0]), id(person2[0]))


#We copied the whole data from Swen. So the name of person2 is still Sarah. We have to change it to Sarah:

person2[0] = "Sarah"

person2[1][0] = "Bücklestrasse"

print(person1, person2)