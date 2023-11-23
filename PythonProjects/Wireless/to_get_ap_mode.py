import re


a = """AP Certificate type                             : Manufacturer Installed Certificate
AP Mode                                         : FlexConnect
AP VLAN tagging state                           : Disabled
AP VLAN tag                                     : 0
CAPWAP Preferred mode                           : IPv4
CAPWAP UDP-Lite                                 : Not Configured
AP Submode                                      : Not Configured
Office Extend Mode                              : Disabled
Dhcp Server                                     : Disabled
Remote AP Debug                                 : Disabled
"""

#b = re.sub(" ", "", a)
c = a.split("\n")
print(c)
for row in c:
    if 'AP Mode' in row:
        key, value = row.split(":")
        mode = value.strip()
        print(mode)
#print(b)