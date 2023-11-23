import csv

from os import walk


path = "C://Users//sackuma3//PycharmProjects//PythonProjects"
f = []
for (root, directories, files) in walk(path):
    for file in files:
        if '.py' in file: ### to read only text file in particuler directories
            print(file)
            #f1 = open(file, 'r')
            #rint(f1.read())


