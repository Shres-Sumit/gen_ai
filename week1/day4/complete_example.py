import requests

def get_posts():
    url = "https://jsonplaceholder.typicode.com/comments"

    try:
        response = requests.get(url)
        response.raise_for_status()

        posts = response.json()

        for post in posts[:3]:
            print("______________")
            print(f"id = {post['id']}")
            print(f"name = {post['name']}")
            print(f"body = {post['body'][:10]}")
            print("_________________")
            print()

    except requests.exceptions.RequestException as e:
        print(e)

get_posts()