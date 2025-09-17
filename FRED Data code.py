import requests
import pandas_datareader.data as web
import datetime


start = datetime.datetime(2000, 1, 1)
end = datetime.datetime(2024, 12, 31)

series_ids = ['GNPCA','GDP', 'UNRATE', 'CPIAUCSL', 'INDPRO']


df = web.DataReader(series_ids, 'fred', start, end)
print(df.head())



    