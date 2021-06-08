# -*- coding: utf-8 -*-
"""
Created on Mon May 10 21:52:07 2021

@author: alvaro
"""


import requests
import pandas as pd

re = requests.get('https://api.binance.com/api/v3/exchangeInfo')
data = re.json()
symbols = data['symbols']

filter_symbol = filter(lambda x: 'USDT' in x['symbol'], symbols)
filter_symbol_status = filter(lambda x: 'USDT' in x['symbol'] and 'TRADING' == x['status'], symbols)

# Lista de diccionarios de mercados con USDT (TRADING & BREAK)
usdt_filter_TB = list(filter_symbol)

# Lista de diccionarios de mercados con USDT, filtrado con mercados activos
usdt_filter = list(filter_symbol_status)

usdt_symbol_list = []

for item in usdt_filter:
    usdt_symbol_list.append(item['symbol'])
    
    
# PRUEBA
usdt_symbol_list = list(filter(lambda x: 'ETHUSDT' == x, usdt_symbol_list))
    

interval = '1d'

for symbol_str in usdt_symbol_list:
    
    print('----------------------------')
    print(f'Downloading {symbol_str} data')
    url = 'https://api.binance.com/api/v3/klines'
    headers = {'accept': 'application/json'}
    doc_columns = ['Open_Time','Open','High','Low','Close','Volume',
                   'Close_Time','Quote_asset_vol','Number_trades','Taker_buy_base',
                   'Taker_buy_quote asset','Ignore']
    
    main_df = pd.DataFrame(columns=doc_columns)
    
    pagination = True
    initial_round = True
    last_end_time = None
    
    while pagination:
        
        try:
            if initial_round:
                print('Initial Round')
                # Se le puede agregar start time y end time
                body = {'symbol':symbol_str, 'interval':interval, 'limit':'1000'}
                initial_round = False
            else:
                body = {'symbol':symbol_str, 'interval':interval, 'limit':'1000', 'endTime':end_time}

            response = requests.get(url, headers=headers, params=body)
            data = response.json()
            print('Data requested')
            
            df = pd.DataFrame(data,columns=doc_columns)
            df['Open_Timestamp'] = pd.to_datetime(df['Open_Time'], unit='ms')
            df['Close_Timestamp'] = pd.to_datetime(df['Close_Time'], unit='ms')
            
            main_df = pd.concat([main_df, df])
            main_df = main_df.sort_values(by='Open_Timestamp', ascending=True)
            end_time = str(main_df['Open_Time'].iloc[0])

            if last_end_time == end_time:
                print('Finishing Fetching')
                break
            last_end_time = end_time
            
        except:
            programation = False
            
    main_df.drop_duplicates(subset ='Open_Time', keep = 'last', inplace = True)
            
    filename = symbol_str + '_' + interval + '.csv'
    print(f'Saving {symbol_str} csv file')
    main_df.to_csv(filename)