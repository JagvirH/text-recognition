from flask import Flask, request, jsonify

app = Flask(__name__)

# Basic route to test the server
@app.route('/')
def home():
    return 'Flask server is running!'

# Simple API that returns personalized greetings
@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    print(data)  # Print the JSON data from the request
    search = data.get('search', '')
    logs = data.get('data', [])
    print(f"Search: {search}")
    for log in logs:
        print(f"ID: {log['id']}, Description: {log['description']}")  # Create personalized greetings
    return jsonify("hi")  # Return the greetings as JSON

if __name__ == '__main__':
    app.run(debug=True)