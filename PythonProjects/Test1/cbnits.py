import re

a = "http://qajenkins01.mgmt.netskope.com:8080/view/NPA%20QE/job/NPA%20run_test%20selector/147/execution/node/3/ws/report_build_147/npa-reports?querystr=123"

a1 = a.split(":")
protocol = a1[0]
print(protocol)
b1 = re.search(r'[0-9]{4}', a)

port = b1.group()
print(port)

url1 = re.sub("//", "", a1[1])

print(url1)

path = re.sub(port, "", a1[2])
print(path)
