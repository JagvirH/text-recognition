from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Basic route to test the server
@app.route('/')
def home():
    return 'Flask server is running!'

# Route for text similarity (implementation to be added)
@app.route('/text-similarity', methods=['POST'])
def text_similarity():
    # Placeholder response for now
    return jsonify({"message": "Text similarity endpoint is working!"})

if __name__ == '__main__':
    app.run(debug=True)


