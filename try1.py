from flask import Flask, request, Response
app = Flask(__name__)

@app.route('/')
def root_response():
    return "Hello World."

@app.route('/api', methods=['POST', 'GET'])
def api_response():
    if request.method == 'POST':
        return request.json

if __name__ == '__main__':
    app.run()
