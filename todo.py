import sqlite3

def run_database_operations():
    sqliteConnection = None
    try:
        # 1. Connect to SQLite Database (creates 'sql.db' if it doesn't exist)
        sqliteConnection = sqlite3.connect('sql.db')
        cursor = sqliteConnection.cursor()
        print('DB Init - Connection established successfully.')

        # 2. Create a table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        print("Table 'users' created or verified.")

        # 3. Insert sample records
        cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
        cursor.execute("INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))
        sqliteConnection.commit()

        # Fetch and display records
        cursor.execute("SELECT * FROM users;")
        print("Initial Records:", cursor.fetchall())

        # 4. Update a record
        cursor.execute("UPDATE users SET name = ? WHERE email = ?", ("Alice Wonderland", "alice@example.com"))
        sqliteConnection.commit()
        print("Record updated successfully.")

        # 5. Delete a record
        cursor.execute("DELETE FROM users WHERE email = ?", ("bob@example.com",))
        sqliteConnection.commit()
        print("Record deleted successfully.")

        # Final check
        cursor.execute("SELECT * FROM users;")
        print("Final Records:", cursor.fetchall())

        # Close the cursor after use
        cursor.close()

    except sqlite3.Error as error:
        print('Error occurred -', error)
        
    finally:
        # Ensure the database connection is closed properly
        if sqliteConnection:
            sqliteConnection.close()
            print('SQLite Connection closed.')

if __name__ == "__main__":
    run_database_operations()