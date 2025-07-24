from data.db_connection import get_connection


def clear_files():
    sql = "DELETE FROM Files"
    conn = None
    try:
        print("Establishing database connection...")
        conn = get_connection()
        print("Database connection established.")
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print("Files table cleared.")
    except Exception as e:
        print(f"Error clearing files: {e}")
    finally:
        if conn:
            conn.close()

def insert_files(files):
    if not files:
        print("No files to insert.")
        return 0

    sql = """
    INSERT INTO Files (
        fileID,
        fileResourceID,
        fileName,
        unitID,
        propertyID
    ) VALUES (?, ?, ?, ?, ?)
    """
    data = [
        (f.file_id, f.file_resource_id, f.file_name, f.file_unit_id, f.file_property_id)
        for f in files
    ]

    conn = None
    try:
        print("Establishing database connection...")
        conn = get_connection()
        print("Database connection established.")
        cursor = conn.cursor()
        cursor.executemany(sql, data)
        conn.commit()
        print(f"{cursor.rowcount} files inserted.")
        return cursor.rowcount
    except Exception as e:
        print(f"Error inserting files: {e}")
        return 0
    finally:
        if conn:
            conn.close()