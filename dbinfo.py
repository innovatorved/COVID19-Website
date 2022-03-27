# database lib
from cloudant import Cloudant
from cloudant.result import Result
import os
# ---------------------------------------------------------------
# parameters for cloudant database

api = os.environ.get('CLOUDANT_DATABASE_KEY')

url_link = os.environ.get('CLOUDANT_URL')

# connect
client = Cloudant.iam(None , api , url = url_link , connect=True)

'''
Access Database Info
'''
db = client['info']
dbMsg = client['msg']
# Access a database
print("Accessing the data . . .")


#print("__Done__")


# ---------------------------------------------------------------

def databaseCloudantExatract():
    """__Extract Information from Cloudant Database__"""
    maildata = set()
    res = Result(db.all_docs, include_docs=True)
    for x in res:
        maildata.add(x['doc']['email'])
    return maildata

def databaseCloudantAdd( name = None , email = None):
    """__Add Name & Email into Database__passes 2 Argument name & email"""
    doc = "__ValueError - Please pass Name & Email__"
    if type(name) != str and type(email) != str: return doc 
    detial = { 'name': name , "email" : email}
    doc = db.create_document(detial)
    return doc

def msgToMe( name = None , email = None , msg = None):
    """Add Messages of Clients in Database"""
    doc = "__ValueError - Please pass Name & Email__"
    if type(name) != str and type(email) != str and type(msg) != str: return doc
    detial = { 'name': name , "email" : email , "Messge" : msg}
    doc = dbMsg.create_document(detial)
    return doc
    