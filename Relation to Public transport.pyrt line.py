import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sodapy import Socrata
import datetime

df = pd.read_csv('Divvy_Trips_2.csv')
  df = pd.read_csv('Divvy_Trips_2.csv')
# df = pd.read_pickle('chicago_1000.pkl')
df
df.columns
Index(['TRIP ID', 'START TIME', 'STOP TIME', 'BIKE ID', 'TRIP DURATION',
       'FROM STATION ID', 'FROM STATION NAME', 'TO STATION ID',
       'TO STATION NAME', 'USER TYPE', 'GENDER', 'BIRTH YEAR', 'FROM LATITUDE',
       'FROM LONGITUDE', 'FROM LOCATION', 'TO LATITUDE', 'TO LONGITUDE',
       'TO LOCATION'],
      dtype='object')

df['FROM LOCATION']
new_data = df.dropna(axis = 0, how = 'any')
new_data
# new_data['start_time'] = pd.to_datetime(new_data['start_time'])
# new_data['stop_time'] = pd.to_datetime(new_data['stop_time'])

# # df['start_date_new'] = df['start_time'].dt.date
# # df['start_time_new'] = df['start_time'].dt.time
# # df['stop_date_new'] = df['start_time'].dt.date
# # df['stop_time_new'] = df['start_time'].dt.time
# # df['new'] = [datetime.datetime.combine(a, b) for a, b in zip(df['s_date'], df['s_time'])]
# # df

new_data['start_year'] = pd.DatetimeIndex(new_data['START TIME']).year
new_data['stop_year'] = pd.DatetimeIndex(new_data['STOP TIME']).year
new_data['stop_year'] = pd.DatetimeIndex(new_data['STOP TIME']).year
new_data['start_month'] = pd.DatetimeIndex(new_data['START TIME']).month
new_data['stop_month'] = pd.DatetimeIndex(new_data['STOP TIME']).month
new_data

new_data.groupby(["stop_year", "stop_month"]).size()

new_data.groupby("stop_month").size()

table_12 = new_data.query("start_month == 6 and stop_month == 6 and start_year == 2014 and stop_year == 2014")
table_12


start_point_6 = table_12.drop(columns=['TRIP ID', 'START TIME', 'STOP TIME',
       'FROM STATION ID', 'TO STATION ID', 'TO STATION NAME', 'USER TYPE', 'GENDER', 'BIRTH YEAR',
       'FROM LOCATION', 'TO LATITUDE', 'TO LONGITUDE',
       'TO LOCATION', 'stop_year', 'stop_month'], axis=1)
start_point_6
start_point_6.to_csv('Start_point_6.csv', index=False)
stop_point_6 = table_12.drop(columns=['TRIP ID', 'START TIME', 'STOP TIME',
       'FROM STATION ID', 'TO STATION ID', 'FROM STATION NAME', 'USER TYPE', 'GENDER', 'BIRTH YEAR',
       'FROM LOCATION', 'FROM LATITUDE', 'FROM LONGITUDE',
       'TO LOCATION', 'start_year', 'start_month'], axis=1)
stop_point_6
stop_point_6.to_csv('stop_point_6.csv', index=False)
