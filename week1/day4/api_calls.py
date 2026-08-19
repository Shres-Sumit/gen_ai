import requests

response = requests.get("https://jsonplaceholder.typicode.com/comments")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"error: {response.status_code}")