import base64

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/decode')
def decode():
    url = request.args.get('url')
    print 'url', url
    raw = requests.get(url)
    print 'raw', raw
    print 'raw.ok', raw.ok
    if raw.ok:
        try:
            return base64.decodestring(raw.text)
        except base64.binascii.Error:
            return 400
    else:
        return 404


@app.route('/encode')
def encode():
    url = request.args.get('url')
    raw = requests.get(url)
    return base64.encodestring(raw)
