import flask
from flask import request, jsonify
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup

app = flask.Flask(__name__)
app.config["DEBUG"] = True

URL = 'https://www.wordreference.com/fren/'


@app.route('/', methods=['GET'])
def home():
    return ''


@app.route('/api/resources/wordref', methods=['GET'])
def api_wordref():
    if 'word' in request.args:
        word = request.args['word']
    else:
        return "Error: No word field provided. Please specify an word."

    req = URL + quote(word)
    print(req)
    resp = requests.get(req)
    soup = BeautifulSoup(resp.content, features='lxml')
    content = soup.find("table", {'class': 'WRD'})
    content = str(content).replace('vtr', 'vtr ').replace('vi', 'vi ').replace('npl', 'npl ')
    content = content.replace('nf', 'nf ')

    return content


app.run()
