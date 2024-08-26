from flask import Flask, request, jsonify
import mysql.connector
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ssl
from transformers import pipeline
from collections import Counter

app = Flask(__name__)

# SSL context handling
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# MySQL database configuration
config = {
    'user': 'root',
    'password': 'jagvir02',
    'host': '127.0.0.1',
    'database': 'personal_health_log',
    'raise_on_warnings': True
}

# Preprocessing function
def preprocess(text):
    # Tokenize the text and convert to lowercase
    tokens = word_tokenize(text.lower())
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Stem the tokens
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    # Join the tokens back into a string
    return ' '.join(tokens)

# Function to fetch and rank logs
def fetch_and_rank_logs(search_text, top_n=5):
    # Establish a connection to the database
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    # Write the SQL query to fetch logs and their tags
    query = """
        SELECT 
            Logs.Id AS logId, 
            Logs.Title AS logTitle, 
            Logs.Description AS logDescription, 
            GROUP_CONCAT(CONCAT(Tags.Title, ' (', Tags.Type, ')')) AS tagDetails
        FROM Logs 
        LEFT JOIN Log_Tags ON Logs.Id = Log_Tags.LogId 
        LEFT JOIN Tags ON Log_Tags.TagId = Tags.Id
        GROUP BY Logs.Id, Logs.Title, Logs.Description;
    """

    # Execute the query and fetch results
    cursor.execute(query)
    results = cursor.fetchall()

    # Close the cursor and the connection
    cursor.close()
    connection.close()

    # Extract log data into a list of dictionaries
    logs = []
    for row in results:
        logs.append({
            'id': row[0],
            'title': row[1],
            'description': row[2],
            'tags': row[3]
        })

    # Extract descriptions and IDs for TF-IDF processing
    descriptions = [log['description'] for log in logs]
    ids = [log['id'] for log in logs]
    titles = [log['title'] for log in logs]

    # Preprocess descriptions
    preprocessed_descriptions = [preprocess(description) for description in descriptions]

    # Feature extraction using TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_descriptions)

    # Preprocess input search text
    preprocessed_input = preprocess(search_text)

    # Transform input text to TF-IDF representation
    input_tfidf = tfidf_vectorizer.transform([preprocessed_input])

    # Calculate cosine similarity between input text and log descriptions
    similarities = cosine_similarity(input_tfidf, tfidf_matrix)

    # Rank descriptions based on similarity
    ranked_indices = sorted(enumerate(similarities[0]), key=lambda x: x[1], reverse=True)

    # Prepare ranked results
    ranked_results = []
    for idx, similarity in ranked_indices[:top_n]:  # Limit the number of results to top_n
        ranked_results.append({
            'id': ids[idx],
            'title': titles[idx],
            'description': descriptions[idx],
            'tags': logs[idx]['tags'],
            'similarity': similarity * 100  # Convert to percentage
        })

    return ranked_results

@app.route('/get_solutions_summary', methods=['POST'])
def get_solutions_summary():
    # Parse the input JSON data
    data = request.get_json()
    search_text = data.get('search', '')
    
    # Fetch and rank logs, showing only the top 5 results
    ranked_logs = fetch_and_rank_logs(search_text, top_n=6)

    all_solutions = []
    log_ids = []
    tag_counter = Counter()  # Counter to track tag frequencies
    for result in ranked_logs:
        log_id = result["id"]
        log_ids.append(log_id)

        # Establish a connection to the database
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        # Query to get solutions for the log
        query = """
            SELECT Solution FROM Solutions WHERE LogId = %s
        """
        cursor.execute(query, (log_id,))
        solutions = cursor.fetchall()

        # Close the cursor and the connection
        cursor.close()
        connection.close()

        # Collect solutions
        for solution in solutions:
            all_solutions.append(solution[0])

        # Count tags from the ranked logs
        if result['tags']:
            tags = result['tags'].split(',')
            tag_counter.update(tags)

    # Summarize the solutions using a summarization pipeline
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    # Combine all solutions into a single text
    combined_solutions = " ".join(all_solutions)

    # Generate a summary using the summarization pipeline
    summary = summarizer(combined_solutions, max_length=200, min_length=50, do_sample=False)

    # Post-process the summary to make it more instructive
    summary_text = summary[0]['summary_text']
    instructive_summary = f"Based on user experiences, the best solutions include: {summary_text}"

    # Find the top 3 most common tags
    top_tags = tag_counter.most_common(3)
    top_tags_list = [{'tag': tag.split(' (')[0], 'type': tag.split(' (')[1][:-1]} for tag, count in top_tags]

    # Return the top similar log IDs, the instructive summary, and the top 3 tags
    print(top_tags_list)

    response = {
        'log_ids': log_ids,
        'instructive_summary': instructive_summary,
        'top_tags': top_tags_list
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
