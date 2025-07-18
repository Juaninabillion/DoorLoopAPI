import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_user_info():
    api_key = os.getenv("DOORLOOP_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DOORLOOP_API_KEY")

    url = "https://app.doorloop.com/api/users/me"
    headers = {
        "Authorization": f"bearer {api_key}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    user_info = get_user_info()
    print(user_info)