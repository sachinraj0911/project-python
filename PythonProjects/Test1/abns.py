import datetime

'''2022-09-23 17:32:30.817330'''
t1 = str(datetime.datetime.now())
n = t1.split(" ")
n2 = n[1].split(".")
n3 = n[0] + "_" + n2[0]
file_name = "sachin" + n3 + ".txt"
f1 = open(file_name, 'a+')
