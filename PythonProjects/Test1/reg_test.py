import re

dict_a = {"a": {"b": {"c": [{"d": 5}]}}}
a = re.findall(r'\:', str(dict_a))
print("No: of keys: {}".format(len(a)))