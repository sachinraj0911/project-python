import re

input_str="SUNDAY:IPV6-MIXED:ALL;MONDAY:IPV4:ALL;TUESDAY:IPV6-MIXED:ALL;"
output_str = {"IPV6": 2, "IPV4" :1}

dict_a = {}

ipv6 = re.findall(r'IPV6', input_str)
ipv6_count = len(ipv6)
dict_a["IPV6"] = ipv6_count

ipv4 = re.findall(r'IPV4', input_str)
ipv4_count = len(ipv4)
dict_a["IPV4"] = ipv4_count

print(dict_a)


