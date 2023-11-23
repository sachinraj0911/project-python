str1 = "H@RM@N C0NNEC%ED $ERV!CE$"
a = {'@': 'A', '%': 'T', '$': 'S', '!': 'I'}
for (k, v) in a.items():
    if k in str1:
        str1 = str1.replace(k, v)


print(str1)