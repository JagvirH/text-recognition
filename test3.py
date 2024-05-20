from flask import Flask, jsonify

app = Flask(__name__)

# Basic route to test the server
@app.route('/')
def home():
    return 'Flask server is running!'

# Simple API that returns a message
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, world!")

if __name__ == '__main__':
    app.run(debug=True)
