data = {
    'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
    'Student 2': {'Name': 'Sanvi', 'Id': 2, "Age": 22},
    'Student 3': {'Name': 'Rohith', 'Id': 3, "Age": 25},
}

for i in data:
    if (data[i])['Age'] > 20:
        print((data[i])['Name'])
