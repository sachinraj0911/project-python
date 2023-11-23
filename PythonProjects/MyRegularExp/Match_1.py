import re
string1 = "14444hello Cookie is a 6666 word of place Cookie"
pattern = "14444"
y = re.search(pattern, string1) # always find the pattern in beggining, if matched

print(y)