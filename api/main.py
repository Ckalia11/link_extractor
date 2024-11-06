#!/usr/bin/env python

from flask import Flask
from flask import request
from flask import jsonify
import redis
import json
import os
from datetime import datetime

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
    cache_usage = "CACHE HIT"
    json_links = r.get(url)
    if not json_links:
        links = extract_links(url)
        json_links = json.dumps(links, indent=2)
        r.set(url, json_links)
        cache_usage = "CACHE MISS"
    # write to cache log
    with open('./logs/cache_hits.log', 'a') as log_file:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f'{current_time} {url} {cache_usage}' + '\n')
    return json_links

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")