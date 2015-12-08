# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 14:41:34 2015

@author: cyao
"""

import pandas as pd
import os
import time
import numpy as np

# Read in CSV data
data = pd.read_csv('trip_data.csv')

# Convert time strings to timestamps
time_converted = pd.to_datetime(data.Time, format="%m/%d/%Y %H:%M")
data.Time = time_converted

# Circulator
circulator = data[(data.Operator=="DC Circulator") & ((data.Description == "Transfer") | (data.Description == "Entry"))]
len(circulator)

circulator.Change

pd.plot()