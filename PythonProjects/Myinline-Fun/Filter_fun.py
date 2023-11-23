"""filter(fun, seq)"""
#filter(fun, seq)
seq = [0,1,3,5,9,10,12,15]

odd = filter(lambda x : x%2 != 0, seq)
even = filter(lambda x : x%2 == 0, seq)

print(list(odd))
print(list(even))