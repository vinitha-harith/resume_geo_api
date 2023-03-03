import os
import json
from google.cloud import datastore
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
project_id = 'resume-ch'

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
    "Access-Control-Max-Age": "3600",
}


def get_client(project_id):
    return datastore.Client(project_id)


client = get_client(project_id)


@app.route('/geo')
def update_visitor_loc():
    tmp = str(request.environ.get('HTTP_X_FORWARDED_FOR'))
    # client_ip, fwd_ip = tmp.split(",")

    tmp1 = str(request.environ.get('x-client-geo-location'))
    # client_region, client_city = tmp1.split(",")

    # key_v = client.key('Visitors-loc')
    # visitors_loc = datastore.Entity(key_v)
    # visitors_loc["client_city"] = client_city
    # visitors_loc["client_region"] = client_region
    # visitors_loc["update_ts"] = datetime.now()
    # visitors_loc["client_ip"] = client_ip
    # client.put(visitors_loc)

    return (json.dumps({"message": tmp1}), 200, CORS_HEADERS)


@app.route('/')
def hello():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    server_port = os.environ.get('PORT', '8080')
    app.run(debug=False, port=server_port, host='0.0.0.0')
