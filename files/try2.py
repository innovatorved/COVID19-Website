from flask import Flask, render_template
import httplib
import json

app = Flask(__name__)


@app.route('/')
def index():
    connection = httplib.HTTPConnection('api.football-data.org')
    headers = {'X-Auth-Token': 'this is my api token here', 'X-Response-Control': 'minified'}
    connection.request('GET', '/v1/competitions/426/leagueTable', None, headers)
    response = json.loads(connection.getresponse().read().decode())
    return response


if __name__ == '__main__':
    app.run()
