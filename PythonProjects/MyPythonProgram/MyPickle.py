import pickle

list = [1,2,3,4]
file = open("sachin", 'wb')
pickle.dump(list, file)
file.close()

