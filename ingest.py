import os
import argparse
from dotenv import load_dotenv
from client import DoorLoopClient
from lease import Lease
from property import Property

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
            
            all_properties= []         
            properties = client.get_all_properties()
            for property_json in properties:
                prop_obj = Property (
                    propertyid = property_json.get("id",None),
                    propertyclass=  property_json.get("class",None),
                    propertyname = property_json.get("name",None),
                    propertytype=property_json.get("type",None)
                )
                all_properties.append(prop_obj)
            for j in all_properties:
                print(j)       
            
            print(f"Found {len(properties.get('data', []))} properties")
        except Exception as e:
            print(f"Error fetching properties: {e}")

    elif args.target == "leases":
        try:
            all_leases = []
            leases = client.get_all_leases()
            for lease_json in leases:
                lease_obj = Lease(
                    lease_number=lease_json.get("reference"),
                    property_number=lease_json.get("property"),
                    start_date=lease_json.get("start"),
                    end_date=lease_json.get("end"),
                    status=lease_json.get("status"),
                    units=lease_json.get("units"),
                    # lease_type=ltype # Add this field in Lease class
                )
                all_leases.append(lease_obj)    
            print(max([len(x.units) for x in all_leases]))
        except Exception as e:
            print(f"Error fetching leases: {e}")

if __name__ == "__main__":
    main()
