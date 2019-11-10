#!flask/bin/python
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/api/object')
def index():
    with open('data.json', 'r') as infile:
        return json.loads(infile.read())

if __name__ == '__main__':
    app.run(debug=True)