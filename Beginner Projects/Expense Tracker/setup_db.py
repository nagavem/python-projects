import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Creating the expenses table if it doesnt exist
cursor.execute("""

CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    description TEXT                        
 )
""")

# Commit and close the connection
conn.commit()
conn.close()

print("Database setup complete. 'expenses.db' is ready!")