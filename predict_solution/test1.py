import mysql.connector
from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

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
query = """
    SELECT 
        Logs.Id AS logId, 
        Logs.Title AS logTitle, 
        Logs.Description AS logDescription, 
        GROUP_CONCAT(Tags.Title) AS tagTitles 
    FROM Logs 
    LEFT JOIN Log_Tags ON Logs.Id = Log_Tags.LogId 
    LEFT JOIN Tags ON Log_Tags.TagId = Tags.Id
    GROUP BY Logs.Id, Logs.Title, Logs.Description
"""

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
