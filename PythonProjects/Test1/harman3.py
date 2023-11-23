def dict_fun(a):
    for (k, v) in a.items():
        print("{} ==> {}".format(k, v))
        if v.__class__ == dict:
            dict_fun(v)
        elif v.__class__ == list:
            for i in v:
                if i.__class__ == dict:
                    dict_fun(i)
                else:
                    break
        else:
            break


dict_a = {"a": {"b": {"c": [{"d": 5}]}}}
print(dict_fun(dict_a))