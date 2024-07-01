import mysql.connector

# Replace with your MySQL database credentials
config = {
    'user': 'root',
    'password': 'jagvir02',
    'host': '127.0.0.1',  # or 'localhost'
    'database': 'personal_health_log',
    'raise_on_warnings': True
}

# Establish a connection to the database
connection = mysql.connector.connect(**config)

# Create a cursor object
cursor = connection.cursor()

# Write the SQL query
query = "SELECT * FROM Logs"

# Execute the query
cursor.execute(query)

# Fetch all rows from the executed query
results = cursor.fetchall()

# Optionally, fetch column names if you want to include them
column_names = cursor.column_names

# Print the results
for row in results:
    print(row)

# Close the cursor and the connection
cursor.close()
connection.close()
