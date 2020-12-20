#flash framework - which is micro framework

from flask import Flask
from flask import request
import requests
from flask import render_template ,redirect ,url_for ,jsonify
import os

# list name
data = []

app = Flask(__name__, static_url_path='')

port = int(os.getenv('PORT', 8000))

@app.route('/', methods = ['GET','POST'])
def index():
	if request.method == 'POST':
        # print('done')
		if 'name' in request.form and 'email'  in request.form:
			name = request.form['name']
			email = request.form['email']
			global data
			data.append({"name":name , "email":email})
			# print(data)
			return "<script>window.alert('Sucessfully Registered');</script>"
		# else:
                        # print("")
	return app.send_static_file("index.html")

@app.route('/data')
def dataAll():
	return jsonify(data)

'''
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 404
'''

# inbuilt function which takes error as parameter
@app.errorhandler(404)  
def notfound(e):
    return app.send_static_file("error.html")

@app.route('/api/<string:n>/<string:m>/')
def add(n,m):
      pass

if __name__ == '__main__':
    # host='0.0.0.0', 
        app.run(port=port ,debug=True, use_reloader=False)
