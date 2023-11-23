import re

a = " hi this my mac address ff:45:2e:7a:f3:cm:00"

b = re.search(r'[a-z A-Z 0-9]{2}\:[a-z A-Z 0-9]{2}\:[a-z A-Z 0-9]{2}\:[a-z A-Z 0-9]{2}\:[a-z A-Z 0-9]{2}\:[a-z A-Z 0-9]{2}', a)
print(b.group())