mystring = "python is good language"
a = mystring.split(" ")

print(a)
for i in range(len(a)):
    b = a[i][::-1]
    a[i] = b

b = " ".join(a)
print(b)