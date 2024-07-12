from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch-content')
def fetch_content():
    url = 'https://ysscores.com/ar/index'
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    app.run(debug=True, port=5000)
