import pandas as pd
from datetime import datetime
import math
import numpy as np

data = pd.read_csv('./data/ADAUSDT-5m-data.csv')

periods = 5
col = data.loc[:, 'close']

def calculate_moving_average(periods, data, col):
   df = data.copy()
   added = []
   for p in range(1, periods):
      colName = 't_'+str(p)
      added.append(colName)
      df[colName] = df.loc[:, col].shift(p)
   df = df.iloc[periods:, :]
   maName = 'moving_average_p'+str(periods)
   df[maName] = df.sum(axis=1)/periods
   df['delta_p'+str(periods)] = (df[maName] - df.loc[:, col])/df.loc[:, col]
   df = df.drop(columns=added)
   return df

def calculate_gradient(periods, data, col):
   df = data.copy()
   df['shift'] = df.loc[:, col].shift(periods)
   df = df.iloc[periods:, :]
   df['gradient'] = np.degrees(np.arctan((df.loc[:, col] - df.loc[:, 'shift'])/periods))
   return df.drop(columns=['shift'])


df = calculate_moving_average(25, data[['timestamp','close']], 'close')
calculate_gradient(1,  data[['timestamp','close']], 'close')