import re

a = """
Plugs to be turned on

Plug A1: InfeedA_Outlet1

Are you sure? (Y/N): Y
Processing - Please wait or <CR> to continue...

Network Power Switch v2.12     Site: (undefined)

Plug | Name             | Password    | Status | Boot/Seq. Delay | Default |
-----+------------------+-------------+--------+-----------------+---------+
 1   | InfeedA_Outlet1  | (undefined) |   ON   |     0.5 Secs    |   ON    |
 2   | InfeedA_Outlet2  | (undefined) |   ON   |     0.5 Secs    |   ON    |
 3   | InfeedA_Outlet3  | (undefined) |   ON   |     0.5 Secs    |   ON    |
 4   | InfeedA_Outlet4  | (undefined) |   ON   |     0.5 Secs    |   ON    |
 5   | InfeedA_Outlet5  | (undefined) |   ON   |     0.5 Secs    |   ON    |
 6   | InfeedA_Outlet6  | (undefined) |   ON   |     0.5 Secs    |   ON    |
 7   | InfeedA_Outlet7  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
 8   | InfeedA_Outlet8  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
 9   | InfeedB_Outlet1  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
 10  | InfeedB_Outlet2  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
 11  | InfeedB_Outlet3  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
 12  | InfeedB_Outlet4  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
 13  | InfeedB_Outlet5  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
 14  | InfeedB_Outlet6  | (undefined) |   ON   |     0.5 Secs    |   ON    |
 15  | InfeedB_Outlet7  | (undefined) |   ON   |     0.5 Secs    |   ON    |
 16  | InfeedB_Outlet8  | (undefined) |   ON   |     0.5 Secs    |   ON    |
-----+------------------+-------------+--------+-----------------+---------+
"""

b = re.sub(" ", "",a)
port_info = re.findall(r'\|.*\|', b)


d = {}
j = 0
#print(port_info)
list1 = []
for info in port_info:
    list1.append(info.split('|'))
print(list1)

for i in list1:
    #d[i[5]] = i[2]
    d[j] = i[3]
    j += 1

print(d)
