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

# List of log entries for Common Cold
common_cold_entries = [
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Feeling Sick", "I have a runny nose, my throat is sore, and I keep coughing.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Not Feeling Well", "I've been sneezing a lot and my body aches all over.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Cough and Cold", "My nose is stuffy and I have a persistent cough.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Under the Weather", "Feeling really tired and my throat is quite scratchy.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Cold Symptoms", "I've got a sore throat and my nose won't stop running.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Common Cold", "I'm feeling weak, sneezing a lot, and have a mild fever.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Sick and Tired", "I have congestion, a sore throat, and my body feels heavy.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Nasal Congestion", "My nose is completely blocked, and I'm coughing a lot.", "Ongoing", 0, 0)
]

# List of log entries for Influenza (Flu)
flu_entries = [
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Flu Symptoms", "I've been experiencing high fever, chills, and severe muscle aches.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Feeling Very Ill", "I have a high fever, headache, and my whole body aches.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Severe Cough", "My throat hurts, and I have a severe cough with fever.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Chills and Fever", "I'm shivering with chills, and my fever is very high.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Body Aches", "Every part of my body aches, and I have a headache.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Extreme Fatigue", "I feel extremely tired and have a high fever.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Persistent Fever", "My fever won't go down, and I'm sweating a lot.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Flu-like Symptoms", "I've got a headache, sore throat, and my muscles are aching.", "Ongoing", 0, 0)
]

# List of log entries for Gastroenteritis (Stomach Flu)
stomach_flu_entries = [
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Stomach Flu Symptoms", "I've been having severe diarrhea and stomach cramps.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Nausea and Vomiting", "I feel very nauseous and have been vomiting frequently.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Dehydration", "I'm feeling very weak and dehydrated due to frequent diarrhea.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Severe Stomach Pain", "My stomach hurts a lot and I have been experiencing diarrhea.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Constant Vomiting", "I can't keep any food down and have been vomiting constantly.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Abdominal Pain", "I have sharp pains in my abdomen and feel nauseous.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Upset Stomach", "My stomach is upset, and I'm experiencing frequent diarrhea.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Stomach Virus", "I'm vomiting and have severe diarrhea with stomach pain.", "Ongoing", 0, 0)
]

# List of log entries for Migraine
migraine_entries = [
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Migraine Attack", "I have a throbbing headache on one side of my head and feel nauseous.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Severe Headache", "I'm experiencing a severe headache with sensitivity to light and sound.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Aura and Pain", "I see flashes of light and have a pulsating headache.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Nausea and Headache", "My head hurts a lot and I feel very nauseous.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Throbbing Pain", "I have a throbbing headache and can't stand any noise.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Blinding Headache", "My headache is so bad I can't see straight.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Intense Migraine", "I have an intense migraine that is making me feel very ill.", "Ongoing", 0, 0),
    ("user_2ihVad4VpwweI3r4B84SJXxfwIg", "Debilitating Headache", "This migraine is debilitating, and I can't function properly.", "Ongoing", 0, 0)
]

# Function to add log entries
def add_data(entries):
    query = """
    INSERT INTO Logs (Users_Id, Title, Description, Status, Bookmark, Share)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    try:
        for entry in entries:
            cursor.execute(query, entry)
        # Commit the transaction
        connection.commit()
        print("Data inserted successfully")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))

# Function to delete log entries for a specific user
def delete_data(user_id):
    query = """
    DELETE FROM Logs WHERE Users_Id = %s
    """
    try:
        cursor.execute(query, (user_id,))
        # Commit the transaction
        connection.commit()
        print("Data deleted successfully")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))

def choice(param):
    if param == "add_common_cold":
        print("Adding Common Cold data...")
        add_data(common_cold_entries)
    elif param == "add_flu":
        print("Adding Flu data...")
        add_data(flu_entries)
    elif param == "add_stomach_flu":
        print("Adding Stomach Flu data...")
        add_data(stomach_flu_entries)
    elif param == "add_migraine":
        print("Adding Migraine data...")
        add_data(migraine_entries)
    elif param == "delete":
        user_id = "user_2ihVad4VpwweI3r4B84SJXxfwIg"
        print(f"Deleting data for user {user_id}...")
        delete_data(user_id)
    elif param == "remove":
        print("No")

x = input("ENTER (add_common_cold/add_flu/add_stomach_flu/add_migraine/delete/remove): ")
choice(x)

# Close the cursor and the connection
cursor.close()
connection.close()
