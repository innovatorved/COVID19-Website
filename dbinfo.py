# database lib
from cloudant import Cloudant
from cloudant.result import Result

# ---------------------------------------------------------------
# parameters for cloudant database

api = "mtFmNq2TppQsnUV2o8OQqcYEbt1cNnKmUWacbJ9AGK_E"

url_link = "https://b9932f06-c0c7-4666-a9bf-72877bb23d13-bluemix.cloudantnosqldb.appdomain.cloud"

# connect
client = Cloudant.iam(None , api , url = url_link , connect=True)

'''
Access Database Info
'''
db = client['info']
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
	
	
    
    
    
