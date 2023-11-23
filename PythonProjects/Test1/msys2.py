input1 = ['data1: This is a data1', 'data2: This is a data2', 'data3: This is a data3']

output1 = [{'data1': 'This is a data1'}, {'data2': 'This is a data2'}, {'data3': 'This is a data3'}]


def list_of_dict(data):
	d = {}
	b = []
	for i in data:
		k, v = i.split(':')
		d[k] = v.strip()
		b.append(d)
		d = {}
	return b


list1 = list_of_dict(input1)
print(list1)
