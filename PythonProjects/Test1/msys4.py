input1 = ['data1: This is a data1', 'data2: This is a data2', 'data3: This is a data3']

output1 = [{'data1': 'This is a data1'}, {'data2': 'This is a data2'}, {'data3': 'This is a data3'}]


def list_of_str_from_dict(data):
    b = []
    str1 = ""
    for i in data:
        for (k, v) in i.items():
            str1 = k + ":" + " " + v
            b.append(str1)
    return b


def list_of_str_from_dict2(data):
    b = []
    for i in data:
        k, v = list(i.items())[0]
        str1 = k + ": " + v
        b.append(str1)
    return b


list1 = list_of_str_from_dict2(output1)
print(list1)
