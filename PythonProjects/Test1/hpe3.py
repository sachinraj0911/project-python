import re
cmd = """

model     :     abc
version   :     1.2
status    :     connected

"""
c = {}
a = cmd.split("\n")
for line in a:
    if ":" in line:
        key, value = line.split(":")
        k = re.sub(" ", "", key)
        v = re.sub(" ", "", value)
        c[k] = v

print(c)


