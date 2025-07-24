import pyodbc
import os
from dotenv import load_dotenv
from data.db_connection import get_connection

def fetch_residential_expiring_leases():
    conn = None
    sql = """EXEC usp_GetResidentialLeasesEndingIn90Days"""
    try:
        print("Establishing database connection...")
        conn = get_connection()
        print("Database connection established.")
        cursor = conn.cursor()
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()
        return [dict(zip(columns, row)) for row in rows]
    
    except Exception as e:
            print(f"Error fetching commercial lease expirations: {e}")
            return []
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    leases = fetch_residential_expiring_leases()
    for lease in leases:
        print(lease)