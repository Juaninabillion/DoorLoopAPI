import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()
driver = os.getenv("DRIVER")
server = os.getenv("SERVER")
database = os.getenv("DATABASE")
uid = os.getenv("UID")
passwd = os.getenv("PASSWD")
print(        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={uid};"
        f"PWD={passwd};")

def get_connection():
    return  pyodbc.connect(
        f"DRIVER={{{driver}}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={uid};"
        f"PWD={passwd};"
    )
                        
        
