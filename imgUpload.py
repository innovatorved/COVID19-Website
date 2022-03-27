# 0673bf40fb419f6f9ca8c63d45acf28e
# help of imgbb
# change image into url

from requests import post
from base64 import b64encode
from json import loads
import os 

url = 'https://api.imgbb.com/1/upload'
key = os.environ.get('IMGBB_API_KEY')

def upload(loc):
    res = post(
    url, 
    data = {
        'key': key, 
        'image':b64encode(open(loc, 'rb').read()),
    })
    return res


# ----------------------------------


def imgUrl(loc):
    imgfile = upload(loc).content
    imgfile = loads(imgfile)
    # print(imgUrl)
    imgUrl = imgfile["data"]["image"]["url"]
    # print(imgUrl)
    return imgUrl

# ---------------------------------------
