from os import walk


path = "C:\\Users\\sackuma3\\Desktop\\sachin"
f = []
for (dirpath, dirnames, filenames) in walk(path):
    for file in filenames:
        if '.txt' in file and '.txt.' not in file:
            print(file)
            #f1 = open(file, 'r')
            #rint(f1.read())
