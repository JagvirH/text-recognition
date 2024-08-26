import mysql.connector
from collections import Counter

# Database connection configuration
config = {
    'user': 'root',
    'password': 'jagvir02',
    'host': '127.0.0.1',
    'database': 'personal_health_log',
    'raise_on_warnings': True
}

# Connect to the database
connection = mysql.connector.connect(**config)
cursor = connection.cursor()

# SQL query to fetch logs and their tags
query = "SELECT * FROM Log_Tags"
cursor.execute(query)
results = cursor.fetchall()

# Extract the tags
tags = [row[1] for row in results]

# Count occurrences of each tag
tag_counts = Counter(tags)

# Calculate total number of tags
total_tags = sum(tag_counts.values())

# Calculate percentage of each tag
tag_percentages = {tag: (count / total_tags) * 100 for tag, count in tag_counts.items()}

# Identify tags with less than 1% and group them into "Other"
other_tags_percentage = 0
filtered_tag_percentages = {}
for tag, percentage in tag_percentages.items():
    if percentage < 5:
        other_tags_percentage += percentage
    else:
        filtered_tag_percentages[tag] = percentage

# Add the "Other" category if there are tags less than 1%
if other_tags_percentage > 0:
    filtered_tag_percentages["Other"] = other_tags_percentage

# Sort the tags by percentage in descending order
sorted_tags = sorted(filtered_tag_percentages.items(), key=lambda item: item[1], reverse=True)

# Output the results
print("Tag percentages (including 'Other'):")
for tag, percentage in sorted_tags:
    print(f"Tag: {tag}, Percentage: {percentage:.2f}%")
