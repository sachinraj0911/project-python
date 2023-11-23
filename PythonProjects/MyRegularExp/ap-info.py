import re


a = """(kukri-2027) >show ap summary

Number of APs.................................... 5

Global AP User Name.............................. Not Configured
Global AP Dot1x User Name........................ Not Configured
Global AP Dot1x EAP Method....................... EAP-FAST

AP Name                         Slots  AP Model              Ethernet MAC       Location              Country     IP Address       Clients  DSE Location
------------------------------  -----  --------------------  -----------------  --------------------  ----------  ---------------  -------  --------------
AP00C8.8BEE.1EA8                2      AIR-AP1832I-B-K9       00:c8:8b:ee:1e:a8  default location      US          50.50.33.141     0        [0 ,0 ,0 ]
AP4001.7AB2.C030                3      AIR-AP4800-B-K9        40:01:7a:b2:c0:30  default location      US          50.50.33.147     0        [0 ,0 ,0 ]
AP58AC.78DC.AAB0                3      AIR-CAP3802E-B-K9      58:ac:78:dc:aa:b0  default location      US          50.50.33.137     0        [0 ,0 ,0 ]
APE4AA.5D3C.F390                3      AIR-AP1810W-B-K9       e4:aa:5d:3c:f3:90  default location      US          50.50.33.146     1        [0 ,0 ,0 ]
AP7cad.74ff.323a                2      AIR-CAP3702E-A-K9      7c:ad:74:ff:32:3a  default location      US          50.50.33.156     0        [0 ,0 ,0 ]"""


apName = re.findall(r'AP[A-Z 0-9]{4}\.[A-Z 0-9]{4}\.[A-Z 0-9]{4}', a)
iplist = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', a)
b = {}
j = 0
for i in apName:
    b[apName[j]]=iplist[j]
    j+=1


print(b)
print(b['APE4AA.5D3C.F390'])
c = 'AP58AC.78DC.AAB0'
print(c in apName)
print(apName)
