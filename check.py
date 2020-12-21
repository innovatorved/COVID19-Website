# idea failed
##########################################

# not in use
############################################33

# importing the required libraries
import pandas as pd

# Visualisation libraries
# import matplotlib.pyplot as plt

# Disable warnings 
import warnings
warnings.filterwarnings('ignore')

# for getting web contents
import requests

# for scraping web contents
from bs4 import BeautifulSoup , Comment

from pprint import pprint
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

# get data
# link at which web data recides
link = 'https://www.mohfw.gov.in/'

# get web data
req = requests.get(link).content
# parse web data
soup = BeautifulSoup(req, "html.parser")

# -----------------------------------------------------------

try1 = []
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for c in comments:
    # print(c)
    try1.append(c)

# find index
len_ck = []
for x in try1:
  len_ck.append(len(x))

check = max(len_ck)
#print(check)
index = len_ck.index(check)

# extract with the help of index
data = str(try1[index])
# print(data)
print(type(data))
data = BeautifulSoup(data, "html.parser")
print(type(data))

# ---------------------------------------------------------------

# get all the rows in table body
# each row is each state's entry
body = data.find_all('tr')
# print(body)
    
# get the table contents
# ======================

# container for table body / contents
State_data = []

# loop through the body and append each row to body
for tr in body:
    td = tr.find_all(['th', 'td'])
    row = [i.text for i in td]
    State_data.append(row)
# pprint(body_rows)

# ----------------------------------------------------------------

# ----------------------------------------------------------------
y = 0
z = 0
while(z<10):
    for x in State_data:
        if x[0] == '' or x[0] == ' ':
            State_data.remove(x)
    #pprint(body_rows)
    z=z+1

# ----------------------------------------------------------------
# Change value in int
for x in range (len(State_data)):
    for y in range (len(State_data[x])):
        # print(x,y)
        try:
            State_data[x][y] = int(State_data[x][y])
        except:
            pass
# ------------------------------------------------------------------

# divide data
name = []
active = []
discharge = []
death = []
