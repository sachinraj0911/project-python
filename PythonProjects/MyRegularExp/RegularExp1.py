import re
pattern = "14444hello Cookie is a 6666 word of place Cookie"
sequence = '\d+'
y = re.findall(sequence, pattern)

print(y)