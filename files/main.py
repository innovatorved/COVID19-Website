#flash framework - which is micro framework

from flask import Flask
from flask import render_template ,redirect ,url_for

# only a sample file 
# Main file is : login.py
# Genral introduction to Python  flask library

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for("login"))

'''
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def new_user():
    return render_template("Registration.html")

@app.route('/new')
def profile():
	return render_template("profile.html")

'''

if __name__ == '__main__':
    app.run(debug=True)
