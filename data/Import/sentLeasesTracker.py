import pyodbc
import os
from dotenv import load_dotenv
from data.db_connection import get_connection

def insert_lease_to_datesent_table(lease_number):       
    sql = """
    INSERT INTO LeasesSent (
        LeaseNumber
    ) VALUES (?)
    """
    conn = None
    try:
        print("Establishing database connection...")
        conn = get_connection()
        print("Database connection established.")
        cursor = conn.cursor()
        cursor.execute(sql, (lease_number,))
        conn.commit()
        print(f"Lease {lease_number} inserted into LeaseSent table.")
    except Exception as e:
        print(f"Error inserting lease into LeaseSent table: {e}")
    finally:
        if conn:
            conn.close( )