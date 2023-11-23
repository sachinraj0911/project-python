a = "one two three four five six seven"
b = a.split()
print(b)
for i in b:
    #print(b.index(i))
    if (b.index(i))%2 != 0:
        a = i[::-1]
        b.insert((b.index(i)), a)
        b.remove(i)

c = " ".join(b)
print(c)