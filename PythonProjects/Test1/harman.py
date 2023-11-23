dict_a = {"a": {"b": {"c": [{"d": 5}]}}}
a = str(dict_a)
b = a.split(":")
dict_b = {}
def dict_fun(a1):
    c = {}
    for (k, v) in a1.items():
        c[k] = v
    return c


for (k, v) in dict_a.items():
    dict_b[k] = v
    if v.__class__ == dict:
        for i in range(len(b) - 2):
            res = dict_fun(v)
            dict_b.update(res)
    else:
        break

print(res)
