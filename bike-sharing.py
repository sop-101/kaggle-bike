import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import missingno as msno
import sys

#importing data set
train = pd.read_csv('bike-sharing-demand/train.csv')
test = pd.read_csv('bike-sharing-demand/test.csv')

#print(train.head()) check to see if csv file has been read properly
df = pd.DataFrame(train)

#split datetime
#df['year'] = pd.DatetimeIndex(df['datetime']).year
df['month'] = pd.DatetimeIndex(df['datetime']).month
df['hour'] = pd.DatetimeIndex(df['datetime']).hour
df['weekday'] = pd.DatetimeIndex(df['datetime']).weekday

#sys.exit()
#replace season and weather 
df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['weather'] = df['weather'].map({1: 'Clear,Few clouds,Partly cloudy',
                                   2: 'Mist + cloudy, Mist + broken clouds, Mist + few clouds, Mist',
                                   3: 'Light Snow, Light Rain + Thunderstorm + Scattered Clouds, Light Rain + Scattered Clouds',
                                   4: 'Heavy Rain + Ice pellets + Thunderstorm + Mist, Snow + Fog'})

catVarList = ['month','hour','weekday','season','weather','holiday','workingday']
for cat in catVarList:
    df[cat] = df[cat].astype('category')
    
df = df.drop(columns=['datetime'])

#find out missing values using missingno
msno.matrix(df,figsize=(20,5))

#determine where the outliers lie
fig, axes = plt.subplots(nrows=2,ncols=2)