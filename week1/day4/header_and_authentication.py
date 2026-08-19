import requests

def header_and_authentication():
    url = "https://jsonplaceholder.typicode.com/comments"
    headers = {
        "Authentication " : "Bearer Token",
        "Content_Type" : "application/json",
        "User_Agent" : "MyApp/1.0"
    }

    response = requests.get(url,headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Authentication failed: {response.status_code}")
        return None

header_and_authentication()