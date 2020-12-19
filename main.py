#flash framework - which is micro framework

from flask import Flask
from flask import request
import requests
from flask import render_template ,redirect ,url_for ,jsonify

#list name
data = []

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
	if request.method == 'POST':
        #print('done')
		if 'name' in request.form and 'email'  in request.form:
			name = request.form['name']
			email = request.form['email']
			global data
			data.append({"name":name , "email":email})
			#print(data)
			return "<script>window.alert('Sucessfully Registered');</script>"
		#else:
                        #print("")
	return render_template("index.html")

@app.route('/data')
def dataAll():
	return jsonify(data)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 404

@app.route('/api/<string:n>/<string:m>/')
def add(n,m):
      pass

if __name__ == '__main__':
        app.run(debug=True, use_reloader=False)
