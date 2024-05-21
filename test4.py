from flask import Flask, request, jsonify
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ssl

app = Flask(__name__)

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Preprocessing function
def preprocess(text):
    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    search_text = data.get('search', '')
    logs = data.get('data', [])
    
    # Extract descriptions and ids
    descriptions = [log['description'] for log in logs]
    ids = [log['id'] for log in logs]
    
    # Preprocess descriptions
    preprocessed_descriptions = [preprocess(description) for description in descriptions]
    
    # Feature extraction using TF-IDF
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_descriptions)
    
    # Preprocess input search text
    preprocessed_input = preprocess(search_text)
    
    # Transform input text to TF-IDF representation
    input_tfidf = tfidf_vectorizer.transform([preprocessed_input])
    
    # Calculate cosine similarity
    similarities = cosine_similarity(input_tfidf, tfidf_matrix)
    
    # Rank descriptions based on similarity
    ranked_indices = sorted(enumerate(similarities[0]), key=lambda x: x[1], reverse=True)
    
    # Prepare ranked results
    ranked_results = []
    for idx, similarity in ranked_indices:
        ranked_results.append({
            'id': ids[idx],
            'description': descriptions[idx],
            'similarity': similarity * 100  # Convert to percentage
        })
    
    return jsonify(ranked_results)

if __name__ == '__main__':
    app.run(debug=True)
