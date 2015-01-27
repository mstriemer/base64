import base64

import requests
from flask import Flask, abort, request

app = Flask(__name__)


@app.route('/decode')
def decode():
    url = request.args.get('url')
    raw = requests.get(url)
    if raw.ok:
        try:
            return (base64.decodestring(raw.text),
                    200,
                    {'Content-type': 'image/png'})
        except base64.binascii.Error:
            return abort(400)
    else:
        return abort(404)
