# https://www.mohfw.gov.in/data/datanew.json

# for getting web contents
from requests import get

#from prettytable import PrettyTable
from matplotlib import pyplot as plt
from datetime import datetime ,  timedelta 

#from pprint import pprint

import json
#import Image

# importing the required libraries
import pandas as pd
import numpy as np
# change image into url
from imgUpload import imgUrl
# importing the required libraries
import pandas as pd

from fbprophet import Prophet
from fbprophet.plot import plot_plotly, add_changepoints_to_plot

from statsmodels.tsa.arima_model import ARIMA

#from datetime import timedelta 
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
    del data_Container[y-1]
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

    confirmed_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    deaths_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    recovered_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    latest_data = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/04-04-2020.csv')
    dates = list(confirmed_df.columns[4:])
    dates = list(pd.to_datetime(dates))
    dates_india = dates[8:]

    tes = list(pd.to_datetime(dates))
    dates_india = dates[8:]
    df1 = confirmed_df.groupby('Country/Region').sum().reset_index()
    df2 = deaths_df.groupby('Country/Region').sum().reset_index()
    df3 = recovered_df.groupby('Country/Region').sum().reset_index()
    # print(df1,df2,df3)
    k = df1[df1['Country/Region']=='India'].loc[:,'1/30/20':]
    india_confirmed = k.values.tolist()[0] 

    k = df2[df2['Country/Region']=='India'].loc[:,'1/30/20':]
    india_deaths = k.values.tolist()[0] 

    k = df3[df3['Country/Region']=='India'].loc[:,'1/30/20':]
    india_recovered = k.values.tolist()[0] 

    plt.figure(figsize= (15,10))
    plt.xticks(rotation = 90 ,fontsize = 11)
    plt.yticks(fontsize = 10)
    plt.xlabel("Dates",fontsize = 20)
    plt.ylabel('Total cases',fontsize = 20)
    plt.title("Total Confirmed, Active, Death in India" , fontsize = 20)

    ax1 = plt.plot_date(y= india_confirmed,x= dates_india,label = 'Confirmed',linestyle ='-',color = 'b')
    ax2 = plt.plot_date(y= india_recovered,x= dates_india,label = 'Recovered',linestyle ='-',color = 'g')
    ax3 = plt.plot_date(y= india_deaths,x= dates_india,label = 'Death',linestyle ='-',color = 'r')
    plt.legend()
    plt.savefig('img/total.jpg')

    k = df1[df1['Country/Region']=='India'].loc[:,'1/22/20':]
    india_confirmed = k.values.tolist()[0] 
    data = pd.DataFrame(columns = ['ds','y'])
    data['ds'] = dates
    data['y'] = india_confirmed

    confirmed = data.copy()
    confirmed.columns = ['ds','y']
    # confirmed['ds'] = confirmed['ds'].dt.date
    confirmed['ds'] = pd.to_datetime(confirmed['ds'])
    prop = Prophet(interval_width=0.95 , daily_seasonality=True)
    prop.fit(data)
    future = prop.make_future_dataframe(periods=15)
    future.tail(15)
    #predicting the future with date, and upper and lower limit of y value
    forecast = prop.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()
    confirmed_forecast_plot = prop.plot(forecast)
    confirmed_forecast_plot = prop.plot(forecast)
    confirmed_forecast_plot =prop.plot_components(forecast)

    arima = ARIMA(data['y'], order=(5, 1, 0))
    arima = arima.fit(trend='c', full_output=True, disp=True)
    forecast = arima.forecast(steps= 30)
    pred = list(forecast[0])

    start_date = data['ds'].max()
    prediction_dates = []
    for i in range(30):
        date = start_date + timedelta(days=1)
        prediction_dates.append(date+timedelta(days=1))
        start_date = date
    plt.figure(figsize= (15,10))
    plt.xlabel("Dates",fontsize = 20)
    plt.ylabel('Total cases',fontsize = 20)
    plt.title("Predicted Values for the next 15 Days" , fontsize = 20)
    # pre = list(enumerate(data['y']))[-1][1]
    # dataprint = {}
    add = ""
    for x in range (0, 15):
        add = add + str(list(prediction_dates)[x])[0:10]+" : "+str(pred[x])+"\n"
    x = x + 1
    plt.plot_date(y= pred,x= prediction_dates,linestyle ='dashed',color = '#ff9999',label = add + "\nNote : Please Ignore the dot value it is a part of Calculation \n")
    add2 = str(list(prediction_dates)[0])[0:10]+" : "+ str(list(enumerate(data['y']))[-1][1])

    plt.plot_date(y=data['y'],x=data['ds'],linestyle = '-',color = 'blue',label = "Actual " + add2)
    plt.legend()
    plt.savefig('img/predict.jpg')
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
    q = imgUrl('img/total.jpg')
    w = imgUrl('img/predict.jpg')
    return [x,y,z,q,w]
