from data.db_connection import get_connection



def clear_units():
    sql = "DELETE FROM Units"
    conn = None
    try:
        print("Establishing database connection...")
        conn = get_connection()
        print("Database connection established.")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Units table cleared.")
    except Exception as e:
        print(f"Error clearing units: {e}")
    finally:
        if conn:
            conn.close()




def insert_units(units):
    if not units:
        print("No units to insert.")
        return 0

    sql = """
    INSERT INTO Units (
        UnitID,
        UnitName,
        UnitAddress,
        PropertyID,
        Status,
        Description)
    VALUES (?,?, ?, ?, ?, ?)
    """

    data = [
        (   u.unitid,
            u.unitname,
            " ".join(str(v) for _, v in u.unitaddress.items()) if isinstance(u.unitaddress, dict) else (u.unitaddress or ""),
            u.unit_propertyid,
            u.unitstatus,
            u.unitdescription
        )
        for u in units
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
