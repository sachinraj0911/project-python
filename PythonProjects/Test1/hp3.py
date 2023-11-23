import requests


url = "https://<ip>/mount_point"
a = requests.get(url)
b = a.json()


