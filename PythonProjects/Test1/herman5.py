def dict_fun(a, b):
    for (k, v) in a.items():
        b[k] = v
        if v.__class__ == dict:
            dict_fun(v, b)
        elif v.__class__ == list:
            for i in v:
                if i.__class__ == dict:
                    dict_fun(i, b)
                else:
                    break
        else:
            break
    return b


dict_a = {"a": {"b": {"c": [{"d": 5}]}}}
b1 = {}

a1 = dict_fun(dict_a, b1)
print(a1)