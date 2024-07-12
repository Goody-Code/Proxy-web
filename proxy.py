from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/fetch-content')
def fetch_content():
    url = 'https://ysscores.com/ar/index'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    target_element = soup.select_one('.championship-wrap.important-matches')
    
    if target_element:
        return jsonify({'content': str(target_element)})
    else:
        return jsonify({'error': 'Element not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
