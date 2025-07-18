import sqlite3

def create_db():
    conn = sqlite3.connect("doorloop_data.db")
    cursor = conn.cursor()

    # Create properties table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS properties (
        id TEXT PRIMARY KEY,
        name TEXT,
        address TEXT
    )
    """)

    # Create units table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS units (
        id TEXT PRIMARY KEY,
        property_id TEXT,
        unit_number TEXT,
        FOREIGN KEY (property_id) REFERENCES properties(id)
    )
    """)

    # Create leases table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leases (
        id TEXT PRIMARY KEY,
        start_date TEXT,
        end_date TEXT,
        status TEXT,
        property_id TEXT,
        unit_id TEXT,
        FOREIGN KEY (property_id) REFERENCES properties(id),
        FOREIGN KEY (unit_id) REFERENCES units(id)
    )
    """)

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_db()
