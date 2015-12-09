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

# Convert time strings to timestamps
time_converted = pd.to_datetime(data.Datetime, format="%m/%d/%Y %H:%M")
data.Datetime = time_converted

# Group into trips based on "Entry"
data['Trip'] = 'NaN'
data.sort(columns = 'Datetime', ascending=True, inplace=True)
i=0
trips= []
for row in data.Description:
    if row == "Entry":
        i += 1    
    trips.append(i)
data['Trip'] = trips

# Examine trips
len(data.Trip.value_counts())

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
subway_df.drop([269, 188], inplace=True) # Drop erroneous trip duration rows

# Period of day
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

# Examine subway trips
subway_df.columns
sum(subway_df.cost) # Total cost
len(subway_df) # Number of trips
len(subway_df.origin.value_counts())
subway_df.period.value_counts()
subway_df.duration.describe() # Total time
subway_df.sort(columns='duration')
subway_df.sort(columns=['origin', 'destination'])[['origin', 'destination', 'duration']]


# Circulator
circulator = data[(data.Operator=="DC Circulator") & ((data.Description == "Transfer") | (data.Description == "Entry"))]
len(circulator)

# Metrobus
data.Trip
