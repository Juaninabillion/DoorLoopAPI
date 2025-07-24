
from data.db_connection import get_connection


def clear_leases():
    sql = "DELETE FROM Leases"
    conn = None
    try:
        print("Establishing database connection...")
        conn = get_connection()
        print("Database connection established.")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Leases table cleared.")
    except Exception as e:
        print(f"Error clearing leases: {e}")
    finally:
        if conn:
            conn.close()

def insert_leases(leases):
    if not leases:
        print("No leases to insert.")
        return 0

    sql = """

    
    INSERT INTO Leases (
        LeaseNumber,
        PropertyNumber,
        StartDate,
        EndDate,
        Status,
        LeaseType,
        Unit
    ) VALUES (?, ?, ?, ?, ?, ?,?)
    """
    print("Preparing data for insertion...")
    data = [
        (
            l.lease_id,
            l.property_number,
            l.start_date,
            l.end_date,
            l.status,
            l.lease_type,
            ' '.join(l.units) if l.units else None  # Assuming units is a list of unit IDs
        )
        for l in leases
    ]
    conn = None
    try:
        print("Establishing database connection...")
        conn = get_connection()
        print("Database connection established.")
        cursor = conn.cursor()
        cursor.executemany(sql, data)
        conn.commit()
        print(f"{cursor.rowcount} units inserted.")
        return cursor.rowcount
    except Exception as e:
        print(f"Error inserting units: {e}")
        return 0
    finally:
        if conn:
            conn.close()
    
def insert_lease_to_datesent_table(lease_number):       
    sql = """
    INSERT INTO LeaseSent (
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
