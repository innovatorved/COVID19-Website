# https://www.mohfw.gov.in/data/datanew.json

# for getting web contents
from requests import get

#from prettytable import PrettyTable
from matplotlib import pyplot as plt
from datetime import datetime

from pprint import pprint

import json
#import Image

# importing the required libraries
import pandas as pd

# change image into url
from imgUpload import imgUrl

import numpy as np
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

def change_to_int(a):
    try:
        b = int(a)
    except ValueError:
        b = 0
    return(b)
# --------------------------------------------------------------------------
def retry():
    url = "https://www.mohfw.gov.in/data/datanew.json"
    web_content = get(url).content

    data = json.loads(web_content)
    # pprint(data)
    # type(data)

    # ----------------------------- data preprocessing

    new_column = ["State_name" , "Active_cases" , "Positive" , "Cured" , "Death" ]
    data_Container = []
    name =[]
    active = []
    Cured = []
    death = []
    confirm = []

    for x in data:
        # print(x)
        new = [x['state_name'] , x['new_active'] , x['new_positive'] , x['new_cured'] , x['new_death']]
        data_Container.append(new)
        
    y = len(data_Container)
    # print(y)
    del data_Container[y-1]
    # print(data_Container)
            
            
    # [['Andaman and Nicobar Islands', '88', '4875', '4732', '61'],
    # ------------------------------------------------------------------------------------
    '''
    time = datetime.now()
    string = str(time)
    time = string.replace(':',' ')
    # print(time)

    with open('Datacorona/COVID19'+time+".txt" , 'w') as file:
        file.write('["State_name" , "Active_cases" , "Positive" , "Cured" , "Death" ]' +"\n")
        for info in data_Container:
           file.write(str(info)+"\n")
    '''
    # -------------------------------------------------------------
    # data distributed into parts
    for x in data_Container:
        name.append(x[0])
        active.append(change_to_int(x[1]))
        confirm.append(change_to_int(x[2]))
        Cured.append(change_to_int(x[3]))
        death.append(change_to_int(x[4]))

    name = np.array(name)
    active = np.array(active,dtype = "int32")
    Cured = np.array(Cured,dtype = "int32")
    confirm = np.array(confirm,dtype = "int32")
    death = np.array(death,dtype = "int32")
    
    '''
    table = PrettyTable()
    table.field_names = (new_column)

    for i in data_Container:
        table.add_row(i)
    table.add_row(["Total", 
                   sum(active), 
                   sum(Cured), 
                   sum(death),
                   sum(confirm)])
    # print(table)
    '''

    # ------------------------------------------------------------------------
    # Data Visulalisation
    plt.figure(figsize = (15,10))
    plt.barh(name,active,align = 'center',color='lightblue',edgecolor='blue',label=' ')
    plt.title('Total Active Case StateWise',fontsize = 18)
    plt.xlabel('No. of Active cases',fontsize = 18)
    plt.ylabel('States/UT',fontsize = 18)
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 7)
    for index, value in enumerate(active):
        plt.text(value, index, str(value), fontsize = 8)
    plt.legend()
    plt.savefig('img/active.jpg')

    c=(sum(confirm))
    r=(sum(Cured))
    d=(sum(death))
    re=(sum(active))

    plt.figure(figsize = (15,10))
    plt.barh(name,Cured,align = 'center',color='lightblue',edgecolor='blue',label = ' ')
    plt.title('Total Cured Case StateWise',fontsize = 18)
    plt.xlabel('No. of Cured cases',fontsize = 18)
    plt.ylabel('States/UT',fontsize = 18)
    plt.xticks(fontsize = 8)
    plt.yticks(fontsize = 7)

    for index, value in enumerate(Cured):
        plt.text(value, index, str(value), fontsize = 8)
    plt.legend()
    plt.savefig('img/cured.jpg')

    group_size = [c,r,d,re]
    group_labels = ['\n\nConfirmed :\n ' + str(c), 
                    '\n\nCured :\n' + str(r), 
                    '\n\n------Death :\n'  + str(d),
                    '\n\nTotal Active Cases \n: ' +str(re)]
    custom_colors = ['skyblue','yellowgreen','tomato','orange']
    plt.figure(figsize = (5,5))
    plt.pie(group_size, labels = group_labels, colors = custom_colors, startangle=60 ,explode=(0.1,0.1,0.1,0.3))
    central_circle = plt.Circle((0,0),0.5, color = 'white')
    fig = plt.gcf()
    fig.gca().add_artist(central_circle)
    plt.rc('font', size = 12) 
    plt.title('Nationwide total Active,\n Confirmed, Cured and Deceased Cases', fontsize = 16)
    plt.savefig('img/death.jpg')
    
#plt.show()

# ----------------------------------------------------------------------------------------------------------------------

# change plot into the form of image
#plt.savefig('img/activeplot.jpg')
#Image.open('testplot.png').save('testplot.jpg','JPEG')

def done():
    # retry()
    """_it gives the image url file_
        no value entered as parameter
    """
    x = imgUrl('img/active.jpg')
    y = imgUrl('img/cured.jpg')
    z = imgUrl('img/death.jpg')
    return [x,y,z]
