import re


def get_valid_ip(datalist):

    # data = " i am host and my ip is 256.19.12.44 5555.555.66.255 you can reach to me with this ip"
    ip = re.search(r'\d{1,3}(\.\d{1,3}){3}', datalist)
    ipadr = ip.group()
    print(ipadr)
    nums = ipadr.split('.')
    if (0 <= int(nums[0]) <= 255) & (0 <= int(nums[1]) <= 255) & (0 <= int(nums[2]) <= 255) & (0 <= int(nums[3]) <= 255):
        return ipadr
    else:
        return "invalid ip"


# data = "i am host and my network address is 255.19.12.44 5555.555.66.255 you can reach to me with this details"
# ip = get_valid_ip(data)
# print(ip)
