import os
import re

stream = os.popen('ping python.org')
data = stream.read()
ping_output = re.search(r'Lost = (\d+) \((\d+)\% loss\)', data)
if ping_output:
    ping_percent = ping_output.group(2)
    if int(ping_percent) <= 10:
        print("PASS-->Ping Succssful")
    else:
        print("Fail===>Ping Fail")

