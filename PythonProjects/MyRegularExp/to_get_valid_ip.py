import re


def to_get_valid_ipaddress(data):
    iplist = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
    valid_ip = []
    for ip in iplist:
        nums = ip.split('.')
        if (0 <= int(nums[0]) <= 255) & (0 <= int(nums[1]) <= 255) & (0 <= int(nums[2]) <= 255) & (
                0 <= int(nums[3]) <= 255):
            valid_ip.append(ip)
        else:
            continue
    return valid_ip


# datalist = "i am host and my ip is 255.19.12.44 5555.555.66.255 255.19.212.44  124.19.56.23 you can reach to me with this ip"
# ip_address = to_get_valid_ipaddress(datalist)
# print(ip_address)