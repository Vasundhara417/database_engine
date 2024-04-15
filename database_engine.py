import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )''')

# Insert records into the table
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Jane Doe', 'jane@example.com'))
conn.commit()

# Retrieve records from the table
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print("Users:")
for user in users:
    print(user)

# Update a record in the table
cursor.execute("UPDATE users SET email = ? WHERE name = ?", ('john.doe@example.com', 'John Doe'))
conn.commit()

# Delete a record from the table
cursor.execute("DELETE FROM users WHERE name = ?", ('Jane Doe',))
conn.commit()

# Close the connection
conn.close()
