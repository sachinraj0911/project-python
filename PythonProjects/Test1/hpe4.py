import requests
import json

class A:
    ulr = "https:/a/bc"

    def get1(self):
        try:
            res = requests.get(self.url)

        except Exception as error:
            print("failure to open the url",error)

        data = res.json()
        return data
