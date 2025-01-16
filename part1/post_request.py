import requests

url = "https://httpbin.org/post"
data = {"name": "Plopp", "age": 78}

response = requests.post(url, json=data)

print(response.status_code, response.json())