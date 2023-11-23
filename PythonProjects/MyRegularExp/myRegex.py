import re


data = "i am host and my ip is 255.19.12.44 5555.555.66.255 196.19.12.48 you can reach to me with this ip"
iplist = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
valid_ip=[]
for ip in iplist:
    nums = ip.split('.')
    if (0 <= int(nums[0]) <= 255) & (0 <= int(nums[1]) <= 255) & (0 <= int(nums[2]) <= 255) & (0 <= int(nums[3]) <= 255):
        valid_ip.append(ip)
    else:
        #print("invalid:=", ip)
        continue
print(valid_ip)


