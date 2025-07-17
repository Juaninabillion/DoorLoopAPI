import requests

class DoorLoopClient:
    def __init__(self, api_key: str, base_url: str = "https://api.doorloop.com/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        })

    def get_properties(self):
        """Example: Fetch all properties (paginated if necessary)."""
        url = f"{self.base_url}/properties"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

def main():
    # Replace with your actual DoorLoop API key
    api_key = "YOUR_API_KEY_HERE"
    
    client = DoorLoopClient(api_key)

    try:
        properties = client.get_properties()
        print("Properties:")
        for prop in properties.get('data', []):
            print(f"- {prop.get('name')} (ID: {prop.get('id')})")
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")

if __name__ == "__main__":
    main()