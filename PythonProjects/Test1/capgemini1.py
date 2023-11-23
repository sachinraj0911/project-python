import os
import re


def localhost_info(localhot):
    c = {}
    stream = os.popen("ping {}".format(localhot))
    data = stream.read()
    if "request could not find" not in data:
        ping_test = re.search(r'Packets: Sent = (\d+), Received = (\d+), Lost = (\d+)', data)
        c['Sent'] = ping_test.group(1)
        c['Received'] = ping_test.group(2)
        c['Lost'] = ping_test.group(3)
        return c
    else:
        print("Ping request could not find host")



a = "kk.com"

b = localhost_info(a)
print(b)

