import os
import requests

class DoorLoopClient:
    def __init__(self, api_key: str, base_url: str = "https://app.doorloop.com/api"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def get_properties(self, page=1, limit=100):
        url = f"{self.base_url}/properties"
        params = {"page": page, "limit": limit}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_user_info(self):
        url = f"{self.base_url}/users/me"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    
    def get_leases(self, page=1, limit=100, **filters):
        url = f"{self.base_url}/leases"
        params = {"page": page, "limit": limit, **filters}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
