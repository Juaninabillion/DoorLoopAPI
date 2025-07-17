import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_login():
    api_key = os.getenv("DOORLOOP_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DOORLOOP_API_KEY in environment")

    url = "https://app.doorloop.com/api/accounts"
    headers = {
        "Authorization": f"bearer {api_key}",  # lowercase per your cURL
        "Accept": "application/json",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        print("✅ Login successful. Response:")
        print(response.json())
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err} - {response.text}")
    except Exception as err:
        print(f"❌ Other error occurred: {err}")

if __name__ == "__main__":
    test_login()
