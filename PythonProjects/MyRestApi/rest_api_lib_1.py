
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class rest_api_lib:
    def __init__(self, vmanage_ip, username, password):
        self.vmanage_ip = vmanage_ip
        self.session = {}
        self.login(self.vmanage_ip, username, password)
    def login(self, vmanage_ip, username, password):

        base_url = 'https://%s:8443/' % (self.vmanage_ip)
        login_action = '/j_security_check'
        # Format data for loginForm
        login_data = {'j_username': username, 'j_password': password}
        # URL for posting login data
        login_url = base_url + login_action
        # URL for retrieving client token
        token_url = base_url + 'dataservice/client/token'
        sess = requests.session()
        # If the vmanage has a certificate signed by a trusted authority change verify to True
        login_response = sess.post(url=login_url, data=login_data, verify=False)
        if b'<html>' in login_response.content:
            print("Login Failed")
            exit(0)
        # update token to session headers
        login_token = sess.get(url=token_url, verify=False)
        if login_token.status_code == 200:
            if b'<html>' in login_token.content:
                print("Login Token Failed")
                exit(0)
            sess.headers['X-XSRF-TOKEN'] = login_token.content
            self.session[vmanage_ip] = sess

    def get_request(self, mount_point):
        """GET request"""
        url = "https://%s:8443/dataservice/%s" % (self.vmanage_ip, mount_point)
        print(url)
        response = self.session[self.vmanage_ip].get(url, verify=False)
        data = str(response.content, encoding = 'utf-8')
        return data