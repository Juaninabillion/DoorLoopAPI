import os
import argparse
from dotenv import load_dotenv
from Clients.client import DoorLoopClient
from models.lease import Lease
from models.property import Property
from models.unit import Unit
from models.file import File
from data.unit_repository import insert_units, clear_units
from data.property_repository import insert_properties, clear_properties
from data.lease_repository import insert_leases, clear_leases
from data.file_repository import insert_files, clear_files


def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Ingest data from DoorLoop API.")
    parser.add_argument("target", choices=["units", "properties", "leases","files"], help="What data to fetch")
    args = parser.parse_args()

    # Load environment variables
    load_dotenv()
    api_key = os.getenv("DOORLOOP_API_KEY")
    
    if not api_key:
        raise RuntimeError("Missing DOORLOOP_API_KEY environment variable")

    # Initialize DoorLoop client
    client = DoorLoopClient(api_key)

    # Conditional execution
    if args.target == "units":
        try:
            all_units= []         
            units = client.get_all_units()
            for unit_json in units:
                unit_obj = Unit (
                    unitid=unit_json.get("id", None),
                    unitaddress=unit_json.get("address", None),
                    unitname=unit_json.get("name", None),
                    unit_propertyid=unit_json.get("property", None),
                    unitstatus=unit_json.get("active", None),
                    unitdescription=unit_json.get("description", None)
                )
                all_units.append(unit_obj)
            #insert units into the database
            clear_units()  # Clear existing units before inserting new ones
            print(f"Cleared existing units from the database.")
            inserted_count = insert_units(all_units)
            print(f"Inserted {inserted_count} units into the database.")
    
        except Exception as e:
            print(f"Error fetching units: {e}")

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
            # Insert properties into the database  
            clear_properties()  # Clear existing properties before inserting new ones
            print(f"Cleared existing properties from the database.")
            inserted_count = insert_properties(all_properties)
            print(f"Inserted {inserted_count} properties into the database.")

        except Exception as e:
            print(f"Error fetching properties: {e}")

    elif args.target == "leases":
        try:
            all_leases = []
            print
            leases = client.get_all_leases()
            for lease_json in leases:
                lease_obj = Lease(
                    lease_id=lease_json.get("id"),
                    property_number=lease_json.get("property"),
                    start_date=lease_json.get("start"),
                    end_date=lease_json.get("end"),
                    status=lease_json.get("status"),
                    units=lease_json.get("units"),
                    
                )
                all_leases.append(lease_obj)
            #insert leases into the database
            clear_leases()  # Clear existing leases before inserting new ones
            print(f"Cleared existing leases from the database.")
            inserted_count = insert_leases(all_leases)
 
        except Exception as e:
            print(f"Error fetching leases: {e}")
    elif args.target == "files":
        try:
            print("Fetching files from the API...")
            # Assuming the client has a method to fetch files
            all_files = []
            files = client.get_all_files()
            for file_json in files:
                file_obj = File(
                    file_id=file_json.get("id"),
                    file_resource_id=file_json.get("linkedResource",{}).get("resourceId"),
                    file_name=file_json.get("name"),
                    file_unit_id=file_json.get("unit"),
                    file_property_id=file_json.get("property")   
                )
                all_files.append(file_obj)
            # Insert files into the database
            clear_files()  # Clear existing files before inserting new ones
            print(f"Cleared existing files from the database.")
            inserted_count = insert_files(all_files)
            print(f"Inserted {inserted_count} files into the database.")
                
        except Exception as e:
            print(f"Error fetching files: {e}")


if __name__ == "__main__":
    main()
