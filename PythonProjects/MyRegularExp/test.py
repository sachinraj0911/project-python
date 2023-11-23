from MyRegularExp.to_get_valid_ip import *

f1 = open("file1", 'r')
ch = f1.read()

ips = to_get_valid_ipaddress(ch)

print(ips)

