import os
from client import DoorLoopClient
from dotenv import load_dotenv

load_dotenv()  # Load .env file

def main():
    api_key = os.getenv("DOORLOOP_API_KEY")
    if not api_key:
        raise RuntimeError("DOORLOOP_API_KEY is not set")

    client = DoorLoopClient(api_key=api_key)

    all_properties = []
    page = 1
    while True:
        print(f"Fetching page {page}")
        data = client.get_properties(page=page)
        properties = data.get("data", [])
        if not properties:
            break
        all_properties.extend(properties)
        if not data.get("nextPage"):
            break
        page += 1

    print(f"Fetched {len(all_properties)} properties total")
    # Write to file or DB here

if __name__ == "__main__":
    main()
