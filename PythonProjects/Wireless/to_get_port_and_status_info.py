import re

a = """
PLUG    |           NAME           | STATUS | DELAY | DEF | PRI | AMPS |
--------+--------------------------+--------+-------+-----+-----+------+
A1     | Local_InfeedA_Outlet1    | ON     | 0.5 S | ON  |  1  |  0.0 |
A2     | Local_InfeedA_Outlet2    | OFF    | 0.5 S | ON  |  2  |  0.0 |
A3     | Local_InfeedA_Outlet3    | ON     | 0.5 S | ON  |  3  |  0.0 |
A4     | Local_InfeedA_Outlet4    | ON     | 0.5 S | ON  |  4  |  0.0 |
A5     | Local_InfeedA_Outlet5    | OFF    | 0.5 S | ON  |  5  |  0.0 |
A6     | Local_InfeedA_Outlet6    | OFF    | 0.5 S | ON  |  6  |  0.0 |
A7     | Local_InfeedA_Outlet7    | OFF    | 0.5 S | ON  |  7  |  0.0 |
A8     | Local_InfeedA_Outlet8    | ON     | 0.5 S | ON  |  8  |  0.0 |
B1     | Local_InfeedB_Outlet1    | OFF    | 0.5 S | ON  |  9  |  0.0 |
B2     | Local_InfeedB_Outlet2    | ON     | 0.5 S | ON  | 10  |  0.0 |
B3     | Local_InfeedB_Outlet3    | OFF    | 0.5 S | ON  | 11  |  0.0 |
B4     | Local_InfeedB_Outlet4    | OFF    | 0.5 S | ON  | 12  |  0.0 |
B5     | Local_InfeedB_Outlet5    | ON     | 0.5 S | ON  | 13  |  0.0 |
B6     | Local_InfeedB_Outlet6    | ON     | 0.5 S | ON  | 14  |  0.0 |
B7     | Local_InfeedB_Outlet7    | ON     | 0.5 S | ON  | 15  |  0.0 |
"""

b = re.sub(" ", "",a)
c = re.sub('\|', "#", b)
list1 = []

port = "14"
d = {}
for line in c.split('\n'):
    if not ("PLUG" in line) and not ("--------" in line):
        list1.append(line.split('#'))
list2 = []
j = 1
for i in range(1, len(list1)-1):
    #d[list1[i][5]] = list1[i][2]
    #list2.append(list1[i])
    d[j] = list1[i][2]
    j += 1

print(list2)
print(d)

if d[int(port)] == 'ON':
    print("yes")
else:
    print("NO")
