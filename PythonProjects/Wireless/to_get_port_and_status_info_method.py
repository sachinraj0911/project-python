import re

def to_get_the_power_status_and_port_info(output):
    """this functin ll get the power status corresponding to port
        from power table of power cycler"""
    a = re.sub(" ", "", output)
    port_info = re.findall(r'\|.*\|', a)
    print(port_info)
    d = {}
    j = 0
    list1 = []
    for info in port_info:
        print(info)
        list1.append(info.split('|'))
        #print(list1)
    for i in list1:
        d[j] = i[3]## here port and corresponding status has stored in dictionary.
        j += 1
    return d

a = """
38:  Network Power Switch v2.12     Site: (undefined)
39: 
40:  Plug | Name             | Password    | Status | Boot/Seq. Delay | Default |
41:  -----+------------------+-------------+--------+-----------------+---------+
42:   1   | InfeedA_Outlet1  | (undefined) |   ON   |     0.5 Secs    |   ON    |
43:   2   | InfeedA_Outlet2  | (undefined) |   ON   |     0.5 Secs    |   ON    |
44:   3   | InfeedA_Outlet3  | (undefined) |   ON   |     0.5 Secs    |   ON    |
45:   4   | InfeedA_Outlet4  | (undefined) |   ON   |     0.5 Secs    |   ON    |
46:   5   | InfeedA_Outlet5  | (undefined) |   ON   |     0.5 Secs    |   ON    |
47:   6   | InfeedA_Outlet6  | (undefined) |   ON   |     0.5 Secs    |   ON    |
48:   7   | InfeedA_Outlet7  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
49:   8   | InfeedA_Outlet8  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
50:   9   | InfeedB_Outlet1  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
51:   10  | InfeedB_Outlet2  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
52:   11  | InfeedB_Outlet3  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
53:   12  | InfeedB_Outlet4  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
54:   13  | InfeedB_Outlet5  | (undefined) |   OFF  |     0.5 Secs    |   ON    |
55:   14  | InfeedB_Outlet6  | (undefined) |   ON   |     0.5 Secs    |   ON    |
56:   15  | InfeedB_Outlet7  | (undefined) |   ON   |     0.5 Secs    |   ON    |
57:   16  | InfeedB_Outlet8  | (undefined) |   ON   |     0.5 Secs    |   ON    |
58:  -----+------------------+-------------+--------+-----------------+---------+
"""

data = to_get_the_power_status_and_port_info(a)
print(data)
port = "13"

if data[int(port)] == 'ON':
    print("yes")
else:
    print("NO")