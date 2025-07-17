import requests

class DoorLoopClient:
    def __init__(self, api_key: str, base_url: str = "https://api.doorloop.com/v1"):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })
        self.base_url = base_url

    def get_properties(self, page=1, limit=100):
        url = f"{self.base_url}/properties"
        params = {"page": page, "limit": limit}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
