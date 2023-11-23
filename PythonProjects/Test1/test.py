import requests


a = {
  "userId": 2,
  "id": 2,
  "title": "delectus aut autem",
  "completed": "false"
}
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.post(url, json= a)

data = response.text
print(data)


