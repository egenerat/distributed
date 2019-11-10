#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/api/object')
def index():
    with open('data.json', 'r') as infile:
        return json.loads(infile.read())

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)