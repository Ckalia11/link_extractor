#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import jsonify
import redis
import json
import os

from linkextractor import extract_links


app = Flask(__name__)
r = redis.from_url(os.getenv("REDIS_URL", "redis://localhost:6379"))

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/api/<url>"

@app.route("/api/<path:url>")
def api(url):
    qs = request.query_string.decode("utf-8")
    if qs != "":
        url += "?" + qs
    # check redis cache
    json_links = r.get(url)
    if not json_links:
        links = extract_links(url)
        json_links = json.dumps(links, indent=2)
        r.set(url, json_links)
    return json_links

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")