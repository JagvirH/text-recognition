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

def addData():
    try:
        query = """
        INSERT INTO Logs (Users_Id, Title, Description, Status, Bookmark, Share)
        VALUES ('user_2ihVad4VpwweI3r4B84SJXxfwIg', 'Common Cold Symptoms', 'I am experiencing a runny nose, sore throat, cough, and slight body aches. It seems like I have a common cold.', 'Ongoing', 0, 0);
        """
        cursor.execute(query)
        # Commit the transaction
        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))

def choice(param):
    if param == "add":
        print("Adding data...")
        addData()
    elif param == "remove":
        print("No")

x = input("ENTER (add/remove): ")
choice(x)

# Close the cursor and the connection
cursor.close()
connection.close()
