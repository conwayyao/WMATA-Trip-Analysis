# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:41:34 2015

@author: cyao
"""

import pandas as pd
import numpy as np
import datetime

# Read in CSV data
data = pd.read_csv('trip_data.csv')

## Convert time strings to timestamps
time_converted = pd.to_datetime(data.Datetime, format="%m/%d/%Y %H:%M")
data.Datetime = time_converted

## Group into trips based on "Entry"
data['Trip'] = 'NaN'
data.sort_values(by = 'Datetime', ascending=True, inplace=True)
i=0
trips= []
for row in data.Description:
    if row == "Entry":
        i += 1    
    trips.append(i)
data['Trip'] = trips

## Examine trips
len(data.Trip.value_counts())

## Drop erroneous trip duration rows
data.drop(data[data.Trip.isin([184, 188, 269])].index, inplace=True) 

# Calculate subway-to-subway trips
subway_trips=[]
for i in range(1, len(set(data['Trip']))+1):
    this_df = data[(data['Trip'] == i) & (data['Operator'] == 'Metrorail') & ( (data['Description'] == 'Entry') | (data['Description'] == 'Transfer') | (data['Description'] == 'Exit'))]
    if len(this_df) < 2:
        continue
    this_trip = {'trip': i, 'entr_trfr':this_df.iloc[0]['Description']}
    this_trip['entr_trfr'] = this_df.iloc[0]['Description']
    if this_df.iloc[0]['Description'] == 'Transfer':
        this_trip['origin'] = this_df.iloc[0]['Exit']
    else:
        this_trip['origin'] = this_df.iloc[0]['Entry_Route']
    this_trip['destination'] = this_df.iloc[-1]['Exit']
    this_trip['entry_time'] = this_df.iloc[0]['Datetime']
    this_trip['exit_time'] = this_df.iloc[-1]['Datetime']
    this_trip['weekday'] = this_df.iloc[0]['Weekday']
    this_trip['duration'] = this_df.iloc[-1]['Datetime'] - this_df.iloc[0]['Datetime']
    this_trip['cost'] = this_df.iloc[0]['Balance'] - this_df.iloc[1]['Balance']
    this_trip['month'] = this_df.iloc[0]['Month']
    subway_trips.append(this_trip)
    
columns = ['trip', 'month', 'weekday', 'entr_trfr', 'origin', 'destination', 'entry_time', 'exit_time', 'duration', 'cost']
subway_df = pd.DataFrame(subway_trips, columns=columns)
subway_df.set_index('trip', inplace=True)

## Period of day
pd_list = []
for i in subway_df.entry_time:
    if (17 < i.hour < 22):
        pd_list.append('evening')
    elif (6 < i.hour < 11):
        pd_list.append('morning')
    elif (11 < i.hour < 17):
        pd_list.append('midday')
    else:
        pd_list.append('night')
subway_df['period'] = pd_list

## On/off peak? 
weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
weekend = ['Friday', 'Saturday']
subway_df['peak'] = False
for i, row in subway_df.iterrows():
    if ((row['weekday'] in weekday) & (5<(row['entry_time'].hour+row['entry_time'].minute/60.0)<9.5)):
        subway_df.set_value(i, 'peak', True)
    elif ((row['weekday'] in weekday) & (15<row['entry_time'].hour<19)):
        subway_df.set_value(i, 'peak', True)
    elif ((row['weekday'] in weekend) & (row['entry_time'].hour<4)):
        subway_df.set_value(i, 'peak', True)

## Examine subway trips
subway_df.columns
sum(subway_df.cost) # Total cost
subway_df.cost.describe() # Cost description
len(subway_df) # Number of trips
subway_df.entr_trfr.value_counts() # Entries/Transfers
len(subway_df.destination.value_counts()) # Number of stations visited
subway_df.period.value_counts() # Time of day
subway_df.duration.sum() # Total time
subway_df.duration.describe() # Duration description
subway_df.sort_values(by='duration').tail(5) # Longest trips
subway_df.sort_values(by=['origin', 'destination'])[['origin', 'destination', 'duration']]

## Examine peak fare trips
subway_df.peak.value_counts() # Number of peak fare trips
subway_df.groupby(by='peak').duration.describe() # Peak fare duration

# Circulator
circulator = data[(data.Operator=="DC Circulator") & ((data.Description == "Transfer") | (data.Description == "Entry"))]
len(circulator) # Total Circulator boardings
circulator.columns

# Bus trips
bus_sys= ['Metrobus', 'DASH Bus', 'FFC Bus']
bus_descrips = ['Entry', 'Transfer']
bus = data[(data.Operator.isin(bus_sys)) & (data.Description.isin(bus_descrips))]

## Examine bus trips
bus.columns
len(bus) # Number of bus trips
bus.Description.value_counts() # Entry/transfers
len(bus.Entry_Route.value_counts()) # Bus routes
bus.Change.value_counts() # Fares
bus.Weekday.value_counts() # Day of week

# Bus period
bus_pd_list = []
for i in bus.Datetime:
    if (17 < i.hour < 22):
        bus_pd_list.append('evening')
    elif (5 < i.hour < 11):
        bus_pd_list.append('morning')
    elif (11 < i.hour < 17):
        bus_pd_list.append('midday')
    else:
        bus_pd_list.append('night')
bus['period'] = bus_pd_list
bus.period.value_counts()

# Bus duration
trips_with_dash = data[data.Trip.isin(data[data.Operator=='DASH Bus'].Trip.values)]
trips_with_dash['duration'] = trips_with_dash['Datetime'].diff()
multi_trips = trips_with_dash.Trip.value_counts()>1
multi_trips = multi_trips[multi_trips==True].index
sort1 = trips_with_dash[trips_with_dash.Trip.isin(multi_trips)]
sort1[sort1.Description == 'Transfer'][['Trip', 'Operator', 'Description', 'duration']]
            
    
