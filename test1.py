import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources




# Sample dataset
texts = [
    "This is a sample document.",
    "Text similarity is important for many applications.",
    "Natural language processing helps analyze text data.",
    "Python is commonly used for text processing tasks.",
    "Machine learning algorithms can be applied to text data."
]

# Preprocessing
def preprocess(text):
    # Tokenization
    tokens = word_tokenize(text.lower())
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)

# Preprocess all texts
preprocessed_texts = [preprocess(text) for text in texts]

# Feature extraction using TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(preprocessed_texts)

# Input text
input_text = "Text analysis is a crucial part of natural language processing."

# Preprocess input text
preprocessed_input = preprocess(input_text)

# Transform input text to TF-IDF representation
input_tfidf = tfidf_vectorizer.transform([preprocessed_input])

# Calculate cosine similarity between input text and all texts in the dataset
similarities = cosine_similarity(input_tfidf, tfidf_matrix)

# Rank texts based on similarity
ranked_texts = sorted(enumerate(similarities[0]), key=lambda x: x[1], reverse=True)

# Print top N similar texts
top_n = 3
for idx, sim in ranked_texts[:top_n]:
    print(f"Similarity: {sim:.2f}\nText: {texts[idx]}")
    print("----")
