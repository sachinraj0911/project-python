import re
string1 = "14444hello Cookie is a 6666Cookie word of place 45Cookie6"
pattern = "Cookie"
y = re.findall(pattern, string1)
print(len(y))
