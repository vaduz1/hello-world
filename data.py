import os
from urllib.request import urlretrieve
import pandas as pd

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_freemont_data (filename='freemont.csv',url=URL, force_download=False):
    if force_download or not os.path.exists(filename):
        urlretrieve(url,filename)
    data = pd.read_csv('freemont.csv',index_col='Date',parse_dates=True)
    data.columns = ['West','East']
    data['Total'] = data['West'] + data['East']
    return data
