import os
import argparse
from dotenv import load_dotenv
from client import DoorLoopClient
from lease import Lease

def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Ingest data from DoorLoop API.")
    parser.add_argument("target", choices=["user", "properties", "leases"], help="What data to fetch")
    args = parser.parse_args()

    # Load environment variables
    load_dotenv()
    api_key = os.getenv("DOORLOOP_API_KEY")
    
    if not api_key:
        raise RuntimeError("Missing DOORLOOP_API_KEY environment variable")

    # Initialize DoorLoop client
    client = DoorLoopClient(api_key)

    # Conditional execution
    if args.target == "user":
        try:
            user = client.get_user_info()
            print("User Info:")
            print(user)
        except Exception as e:
            print(f"Error fetching user info: {e}")

    elif args.target == "properties":
        try:
            properties = client.get_properties()
            print(f"Found {len(properties.get('data', []))} properties")
            for prop in properties.get("data", []):
                print(f"{prop.get('name')} (ID: {prop.get('id')})")
        except Exception as e:
            print(f"Error fetching properties: {e}")

    elif args.target == "leases":
        try:
            leases = []
            leases = client.get_leases()
            print(f"Found {len(leases.get('data', []))} leases")
            print(leases["data"][0])
            for lease_json in leases.get("data", []):
                lease_obj = Lease(
                    lease_number=lease_json.get("reference"),
                    property_number=lease_json.get("property"),
                address="Address not in lease data",  # You may fetch this separately if needed
                start_date=lease_json.get("start"),
                end_date=lease_json.get("end")
            )
                print(lease_obj)


        except Exception as e:
            print(f"Error fetching leases: {e}")

if __name__ == "__main__":
    main()
