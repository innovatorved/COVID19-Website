import requests
from matplotlib import pyplot as plt
from datetime import datetime ,  timedelta
import pandas as pd
import numpy as np

from base64 import b64encode
from json import loads

import time

from fbprophet import Prophet
from fbprophet.plot import plot_plotly, add_changepoints_to_plot

from statsmodels.tsa.arima_model import ARIMA

urlsend = "http://coronaupdate-impressive-chipmunk-ma.eu-gb.mybluemix.net/senddata"

url = 'https://api.imgbb.com/1/upload'
key = '0673bf40fb419f6f9ca8c63d45acf28e'

def predict():
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
    prop = Prophet(interval_width=0.95)
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
    add2 = str(time.strftime("%Y-%m-%d",time.localtime()))+" : "+ str(list(enumerate(data['y']))[-1][1])

    plt.plot_date(y=data['y'],x=data['ds'],linestyle = '-',color = 'blue',label = "Actual " + add2)
    plt.legend()
    plt.savefig('img/predict.jpg')

# ------------------------------------------
def upload(loc):
    res = requests.post(
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

def done():
    predict()
    """_it gives the image url file_
        no value entered as parameter
    """
    q = imgUrl('img/total.jpg')
    w = imgUrl('img/predict.jpg')
    return [q,w]

# ---------------------------------------
# predict()
data = done()
a = data[0]
b = data[1]

myjson = {'link4': a,'link5': b}

x = requests.post(urlsend, json = myjson)
print (x.content)
