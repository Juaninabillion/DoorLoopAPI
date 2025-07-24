import os
import requests
import time

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

    def get_properties(self, page_number=1, page_size=100, **filters):
        url = f"{self.base_url}/properties"
        params = {"page_number": page_number, "page_size": page_size, **filters}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_leases(self, page_number=1, page_size=100, **filters):
        url = f"{self.base_url}/leases"
        params = {"page_number": page_number, "page_size": page_size, **filters}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_units(self, page_number = 1, page_size = 100, **filters):
         url = f"{self.base_url}/units"
         params = { "page_number":page_number, "page_size":page_size, **filters}
         response = self.session.get(url,params=params)
         response.raise_for_status()
         return response.json()

    def get_files(self, page_number=1, page_size=100, **filters):
        url = f"{self.base_url}/files"
        params = {"page_number": page_number, "page_size": page_size, **filters}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    

    def get_user_info(self):
        url = f"{self.base_url}/users/me"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    


    def get_all_properties(self, page_size=100, **filters):
        all_properties = []
        page_number = 1
        while True:        
            response_json = self.get_properties(page_number = page_number, page_size = page_size, **filters)
            data= response_json.get("data",[])
            all_properties.extend(data)
            total_records = response_json.get("total",0)
            size = response_json.get("page_size", page_size)
            total_pages = (total_records + size - 1) // size
            if page_number >= total_pages or not data:
                print("Reached the last page or no more data.")
                break
            page_number += 1
            time.sleep(0.5)
        return all_properties
    
    def get_all_leases(self, page_size=100, **filters):
        all_leases = []
        page_number = 1

        while True:
            response_json = self.get_leases(page_number=page_number, page_size=page_size, **filters)
            data = response_json.get("data", [])

            all_leases.extend(data)
            print(f"Fetched page {page_number} with {len(data)} leases (total so far: {len(all_leases)})")

            total_records = response_json.get("total", 0)
            size = response_json.get("page_size", page_size)
            total_pages = (total_records + size - 1) // size

            if page_number >= total_pages or not data:
                print("Reached the last page or no more data.")
                break

            page_number += 1
            time.sleep(0.5)

        return all_leases
    
    def get_all_units(self,page_size = 100, **filters):
        all_units = []
        page_number = 1

        while True:
            response_json = self.get_units(page_number=page_number,page_size=page_size,**filters)
            data = response_json.get("data",[])
            all_units.extend(data)
            print(f"Fetched page {page_number} with {len(data)} leases (total so far: {len(all_units)})")

            total_records = response_json.get("total", 0)
            size = response_json.get("page_size", page_size)
            total_pages = (total_records + size - 1) // size

            if page_number >= total_pages or not data:
                print("Reached the last page or no more data.")
                break

            page_number += 1
            time.sleep(0.5)

        return all_units
    
    def get_all_files(self, page_size=100, **filters):
        all_files = []
        page_number = 1

        while True:
            response_json = self.get_files(page_number=page_number, page_size=page_size, **filters)
            data = response_json.get("data", [])
            all_files.extend(data)
            print(f"Fetched page {page_number} with {len(data)} files (total so far: {len(all_files)})")

            total_records = response_json.get("total", 0)
            size = response_json.get("page_size", page_size)
            total_pages = (total_records + size - 1) // size

            if page_number >= total_pages or not data:
                print("Reached the last page or no more data.")
                break

            page_number += 1
            time.sleep(0.5)

        return all_files

    



