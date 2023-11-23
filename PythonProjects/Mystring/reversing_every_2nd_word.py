a = "one two three four five six seven"
b = a.split()
print(b)
for i in range(len(b)-1):
    if i%2 != 0:
        d = b[i][::-1]
        b[i] = d

print(b)
c = " ".join(b)
print(c)