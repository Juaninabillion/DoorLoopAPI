from data.db_connection import get_connection


def clear_properties():
    sql = "DELETE FROM Properties"
    conn = None
    try:
        print("Establishing database connection...")
        conn = get_connection()
        print("Database connection established.")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Properties table cleared.")
    except Exception as e:
        print(f"Error clearing properties: {e}")
    finally:
        if conn:
            conn.close()


def insert_properties(properties):
    if not properties:
        print("No properties to insert.")
        return 0
    
    sql = """
    INSERT INTO Properties (
        PropertyID
        ,PropertyClass
        ,PropertyName
        ,PropertyType)
    VALUES (?, ?, ?, ?)
    """
    print("Preparing data for insertion...")
    data = [
        (p.propertyid
         , p.propertyclass
         , p.propertyname
         , p.propertytype) 
    for p in properties
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
