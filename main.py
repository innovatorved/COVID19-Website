#flash framework - which is micro framework
from flask import Flask
from flask import request
import requests
from flask import render_template ,redirect ,url_for ,jsonify
import os
from EmailSend import email , send
#from time import sleep
# gives covid data
from CoronaData import done
#from datetime import datetime

# for multi processing
# from multiprocessing import Process

# list name
data = []
maildata = set()

app = Flask(__name__, static_url_path='')

port = int(os.getenv('PORT', 8000))

@app.route('/', methods = ['GET','POST'])
def index():
	if request.method == 'POST':
        # print('done')
		if 'name' in request.form and 'email'  in request.form:
			name = request.form['name']
			mail = request.form['email']
			email(name,mail)
			global data
			maildata.add(mail)
			data.append({"name":name , "email":mail})
			# print(data)
			return "<script>window.alert('Successfully Registered'); window.location.href = '/';</script>"
			#return app.send_static_file("index.html")
		# else:
                        # print("")
	return app.send_static_file("index.html")

@app.route('/data/')
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

@app.errorhandler(500)  
def notfound(e):
        return app.send_static_file("error.html")

@app.route('/api/go/')
def add():
        l = done()
        for x in maildata:
                send(l,x)
                #print("done")
        return "<script>window.alert('Done Sir'); window.location.href = '/';</script>" 


@app.route('/api/rm/<string:n>/')
def remove(n):
        maildata.remove(n)
        return "<script>window.alert('Succesfully UnSubscribed'); window.location.href = '/';</script>" 

@app.route('/api/del/')
def dell():
        data.clear()
        maildata.clear()
        return "<script>window.alert('All Data Clear'); window.location.href = '/';</script>" 


if __name__ == '__main__':
        # host='0.0.0.0',
        app.run(host='0.0.0.0',port=port ,debug = True , use_reloader=False)

# release the data


        
        
