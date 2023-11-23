import requests
from rest_api_lib_1 import *

import json

vmanage_ip = "172.27.127.86"
vmanage_username = "admin"
vmanage_password = "Iotbu123!"

vmanage = rest_api_lib(vmanage_ip, vmanage_username, vmanage_password)
vmanage_login = vmanage.login(vmanage_ip, vmanage_username, vmanage_password)

data = vmanage.get_request('device')

loaded_json = json.loads(data)

for k in loaded_json:
    if k == 'data':
        devices_info = loaded_json[k]

        print(devices_info)
