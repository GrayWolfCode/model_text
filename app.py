from flask import Flask, jsonify, request
from flask_cors import CORS

import json


app = Flask(__name__)
CORS(app)


@app.route('/split_text', methods=['POST'])
def split_text():
    data = request.json
    if data and 'text' in data:
        text = data['text']
        parts = text.split('#')  # splitting the text into parts
        return jsonify(parts)  # returning the parts as a JSON array
    else:
        # returning an error if no text is provided
        return jsonify(error="No text provided"), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
