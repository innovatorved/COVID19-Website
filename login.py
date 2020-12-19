##############################################
#         Author : Ved Prakash Gupta         #
##############################################

from flask import Flask , render_template ,request, redirect , session , url_for
from flask_mysqldb import MySQL
import MySQLdb

#########################
#Modules for Email
from emailNextIn import send
from emailNextIn import logOut
###############################
global sub , content
sub = "U are now Connected to NextIn !"

content = '''
			Enter Your Message in this Content Variable
		           - Team NextIn
		'''

#################################
app = Flask(__name__)
app.secret_key = "7007868719"

#connection bettween mysql and python
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "7755011883"
app.config["MYSQL_DB"] = "nextin"

#database
db = MySQL(app)

i = 0

#login page
@app.route('/', methods = ['GET','POST'])
def index():
	if request.method == 'POST':
        #print('done')
		if 'username' in request.form and 'password'  in request.form:
			username = request.form['username']
			password = request.form['password']
			print(username)
			print(password)
			cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute("SELECT * FROM login WHERE email=%s AND pass=%s",(username,password))
			info = cursor.fetchone()
			if info is not None:
				if info['email'] == username and info['pass'] == password:
					if i == 0:
						session["login Succesfull"] = True
					return redirect(url_for("profile"))

			else:
				return redirect(url_for("index"))
	return render_template("login.html")


#register page
@app.route('/new', methods = ['GET','POST'])
def new():
	if request.method == 'POST':
		print("done")
		if "name" in request.form and "num" in request.form and "email" in request.form and "gender" in request.form and "dob" in request.form and "dis" in request.form and "password" in request.form:
			name = request.form["name"]
			number = request.form["num"]
			email = request.form["email"]
			gender = request.form["gender"]
			dob = request.form["dob"]
			district = request.form["dis"]
			password = request.form["password"]
			print("kaam kr rha hai")
			cur = db.connection.cursor(MySQLdb.cursors.DictCursor)
			cur.execute("INSERT INTO nextin.login(myname,DOB,District,Gender,contact_info,email,pass)VALUES(%s, %s, %s, %s, %s, %s, %s)",(name, dob, district, gender, number, email, password))
			db.connection.commit()
			send(email, sub, content)
			return redirect(url_for("index"))
		else:
			return redirect(url_for("new"))
	return render_template("Registration.html")


#profile    
@app.route("/new/profile")
def profile():
    if session["login Succesfull"] == True:
        return render_template("profile.html")

#logout and session destroyed
@app.route("/new/logout")
def logout():
	session.pop("login Succesfull",None)
	return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
