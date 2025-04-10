# -*- coding: utf-8 -*-
"""rate-components.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/scottSart/27f1bcc30aa69d4553501e618e8dfbd8/rate-components.ipynb
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import requests

path = '/content/drive/MyDrive/2025-04-09_Yield Spreads'
os.chdir(path)

# Datasets done : 10 Year inflation,  30 Year Mortgage Rates
## Datasets not done:
  # OAS MBS - Rate aligns with 'FED' datset in excel but does not match the one on the final sheet
  # NY Fed TP
  # MBS Yield

# FRED API KEY

API_KEY = 'd0946ae1532277ebd0b673c18f5283a3'
year10_BE_Inflation = 'T10YIE'
mort_yiled = 'MORTGAGE30US'
mbs_oas = 'BAMLC0A4CBBB'
ny_tp = 'THREEFYTP10'

# Pulling data for 10 year inflation

end_date = datetime.today()
start_date = end_date - timedelta(days=182)  # approx. 6 months

params = {
    'series_id': year10_BE_Inflation,
    'api_key': API_KEY,
    'file_type': 'json',
    'observation_start': start_date.strftime('%Y-%m-%d'),
    'observation_end': end_date.strftime('%Y-%m-%d')
}

url = 'https://api.stlouisfed.org/fred/series/observations'
resp = requests.get(url, params=params)
data = resp.json()['observations']

Y10Inflation = pd.DataFrame(data)
Y10Inflation.drop(columns  = ['realtime_start', 'realtime_end'], inplace = True)
Y10Inflation.rename(columns = {'value':'Y10_Inflation'}, inplace = True)

# Pulling data for 30 year mortgage fixed

end_date = datetime.today()
start_date = end_date - timedelta(days=182)  # approx. 6 months

params = {
    'series_id': mort_yiled,
    'api_key': API_KEY,
    'file_type': 'json',
    'observation_start': start_date.strftime('%Y-%m-%d'),
    'observation_end': end_date.strftime('%Y-%m-%d')
}

url = 'https://api.stlouisfed.org/fred/series/observations'
resp = requests.get(url, params=params)
data = resp.json()['observations']

Y30_MortYield = pd.DataFrame(data)
Y30_MortYield.drop(columns  = ['realtime_start', 'realtime_end'], inplace = True)
Y30_MortYield.rename(columns = {'value':'Y30Mort_Yield'}, inplace = True)

# Getting MBS OAS

end_date = datetime.today()
start_date = end_date - timedelta(days=182)  # approx. 6 months

params = {
    'series_id': mbs_oas,
    'api_key': API_KEY,
    'file_type': 'json',
    'observation_start': start_date.strftime('%Y-%m-%d'),
    'observation_end': end_date.strftime('%Y-%m-%d')
}

url = 'https://api.stlouisfed.org/fred/series/observations'
resp = requests.get(url, params=params)
data = resp.json()['observations']

mbs_oas = pd.DataFrame(data)
mbs_oas.drop(columns  = ['realtime_start', 'realtime_end'], inplace = True)
mbs_oas.rename(columns = {'value':'mbs_oas'}, inplace = True)

# Getting NY FED TP

end_date = datetime.today()
start_date = end_date - timedelta(days=182)  # approx. 6 months

params = {
    'series_id': ny_tp,
    'api_key': API_KEY,
    'file_type': 'json',
    'observation_start': '2023-11-01',
    'observation_end': end_date.strftime('%Y-%m-%d')
}

url = 'https://api.stlouisfed.org/fred/series/observations'
resp = requests.get(url, params=params)
data = resp.json()['observations']

ny_tp = pd.DataFrame(data)
ny_tp.drop(columns  = ['realtime_start', 'realtime_end'], inplace = True)
ny_tp.rename(columns = {'value':'ny_tp'}, inplace = True)