#get request

import requests

def get_user(user_id):
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"id":user_id}

    response = requests.get(url,params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Found {len(data)} posts for user {user_id}")
        print(data)
    return None

get_user(1)

def create_post():
    url ="https://jsonplaceholder.typicode.com/comments"
    new_data = {
    "postId": 3,
    "id": 3,
    "name": "id labore ex et quam laborum",
    "email": "Eliseo@gardner.biz",
    "body": "laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
    }

    response = requests.post(url, json=new_data)

    if response.status_code == 201:
        print("data inseted")

create_post()
    