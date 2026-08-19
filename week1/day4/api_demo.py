import requests
from typing import Dict, List, Optional

class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'MyAPIClient/1.0'
        })
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Optional[Dict]:
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return None
    
    def post(self, endpoint: str, data: Dict) -> Optional[Dict]:
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.post(url, json=data, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Error: {e}")
            return None

# Usage
if __name__ == "__main__":
    client = APIClient("https://jsonplaceholder.typicode.com")
    
    # GET request
    posts = client.get("posts", {"userId": 1})
    if posts:
        print(f"User 1 has {len(posts)} posts")
    
    # POST request
    new_post = client.post("posts", {
        "title": "Test Post",
        "body": "This is a test",
        "userId": 1
    })
    if new_post:
        print(f"Created post ID: {new_post.get('id')}")