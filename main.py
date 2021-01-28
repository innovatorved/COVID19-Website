#flash framework - which is micro framework
from flask import Flask
from flask import request
import requests
from flask import render_template ,redirect ,url_for ,jsonify ,make_response
# from flask import render_template ,redirect ,url_for ,jsonify
import os
from EmailSend import email , send
#from time import sleep
# gives covid data
from CoronaDataNew import done , retry
#from datetime import datetime

# database lib
from dbinfo import databaseCloudantExatract , databaseCloudantAdd

"""
# database lib
from cloudant import Cloudant
from cloudant.result import Result
"""

# for multi processing
# from multiprocessing import Process

# list name
# data = []
# maildata = set()

# ---------------------------------------------------------------
# parameters for cloudant database
'''
api = "mtFmNq2TppQsnUV2o8OQqcYEbt1cNnKmUWacbJ9AGK_E"

url_link = "https://b9932f06-c0c7-4666-a9bf-72877bb23d13-bluemix.cloudantnosqldb.appdomain.cloud"

# connect
client = Cloudant.iam(None , api , url = url_link , connect=True)

# Access a database
print("Accessing the data . . .")

db = client['info']
res = Result(db.all_docs, include_docs=True)

for x in res:
        maildata.add(x['doc']['email'])
print("__Done__")


link = None
link4 = None
link5 = None
'''
# ---------------------------------------------------------------
# Exract Information From Database
maildata = databaseCloudantExatract()

# --------------------------------------------------------------

app = Flask(__name__, static_url_path='')

port = int(os.getenv('PORT', 8000))

@app.route('/', methods = ['GET','POST'])
def index():
	return redirect('main')
	#return app.send_static_file("index.html")

@app.route('/main', methods = ['GET','POST'])
def homepage():
    if request.method == 'POST':
        # print('done')
        if 'name' in request.form and 'email'  in request.form:
            name = request.form['name']
            mail = request.form['email']
            
            if mail in maildata: return "<script>window.alert('E-Mail is Already Registered'); window.location.href = '/main';</script>"               
            # detial = { 'name': name , "email" : mail}
            #   doc = db.create_document(detial)
            
            # Use databaseCloudantAdd() - fun to add data in database
            databaseCloudantAdd(name , mail)
            
            maildata.add(mail)
            email(name,mail)
            return "<script>window.alert('Successfully Registered'); window.location.href = '/main';</script>"
            # return app.send_static_file("index.html")
        # else:
                        # print("")
    return render_template("index.html")

@app.route('/privacy-policy')
def privacy():
	return render_template("privacy.html")

@app.route('/terms-condition')
def terms():
	return render_template("term.html")
    
'''

@app.route('/data/')
def dataAll():
	return jsonify(data)


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
        retry()
        l = done()
        for x in maildata:
                send(l , x)
                print("done")
        #maildata.clear()
        return "<script>window.alert('Done Sir'); window.location.href = '/main';</script>"

@app.route("/sitemap.xml")
def sitemap_xml():
        response= make_response(render_template("sitemap.xml"))
        response.headers['Content-Type'] = 'application/xml'
        return response

@app.route("/main/sitemap.xml")
def sitemapsite():
        resp= make_response(render_template("site.xml"))
        resp.headers['Content-Type'] = 'application/xml'
        return resp

@app.route("/robots.txt")
def robots_txt():
        return render_template("robots.txt")

'''
@app.route('/api/rm/<string:n>/')
def remove(n):
        maildata.remove(n)
        return "<script>window.alert('Succesfully UnSubscribed'); window.location.href = '/';</script>" 


@app.route('/api/del/')
def dell():
        data.clear()
        maildata.clear()
        return "<script>window.alert('All Data Clear'); window.location.href = '/';</script>" 

'''

'''
@app.route('/senddata', methods=['POST'])
def testfn():
    if request.method == 'POST':
        #print()  # parse as JSON
        val = None
        val = request.get_json()
        
        global link , link4, link5
        link4 = val['link4']
        link5 = val['link5']
        link = None
        link = [link4 , link5]
        return 'Sucesss', 200
'''

if __name__ == '__main__':
        # host='0.0.0.0',
        app.run(host='0.0.0.0',port=port ,debug = True , use_reloader=False)

# release the data


        
        
