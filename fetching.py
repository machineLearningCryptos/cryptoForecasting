import requests
import datetime
import pandas as pd

class fetch(object):
    
    def price_history(symbol, comparison_symbol, histoday=True, limit=1, aggregate=1, allData='true'):
        
        # api url
        if histoday:
            url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}&allData={}' \
                .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate, allData)
        else:
            url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}&allData={}' \
                .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate, allData)

        # fetch data
        page = requests.get(url)
        data = page.json()['Data']

        # Convert Json to Table
        df = pd.DataFrame(data)

        # add a column with timestamp
        df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]

        return df

    def media_coverage():
        
        url = 'https://api.gdeltproject.org/api/v2/doc/doc?format=csv&timespan=1y&query=(bitcoin%20OR%20cryptocurrency%20OR%20cryptocurrencies)&mode=timelinevol&timezoom=yes'
        c=pd.read_csv(url, usecols=["Date","Value"])
        c['Date'] = [pd.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in c.Date]
        c = c.set_index('Date')
        
        return c

