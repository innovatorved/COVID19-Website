#flash framework - which is micro framework

from flask import Flask
from flask import render_template ,redirect ,url_for



app = Flask(__name__)

@app.route('/h', methods = ['GET','POST'])
def index():
	if request.method == 'POST':
        #print('done')
		if 'name' in request.form and 'email'  in request.form:
			name = request.form['name']
			email = request.form['email']
			print(name)
			print(email)
	return render_template("index.html")

@app.route('/')
def hello():
	return "hello"
	
if __name__ == '__main__':
        app.run(debug=True, use_reloader=False)
