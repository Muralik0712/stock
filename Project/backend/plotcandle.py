import matplotlib.pyplot as plt
#from mplfinance import candlestick_ohlc
from mplfinance.original_flavor import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpdates
def cplot(fname):
    plt.style.use('dark_background')
    df = fname
    df = df[['Date', 'Open', 'High','Low', 'Close']]
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'].map(mpdates.date2num)
    fig, ax = plt.subplots()
    candlestick_ohlc(ax, df.values, width = 0.6,
                 colorup = 'green', colordown = 'red',
                 alpha = 0.8)
    ax.grid(True)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.title('Prices For the Period 01-07-2020 to 15-07-2020')
    date_format = mpdates.DateFormatter('%d-%m-%Y')
    ax.xaxis.set_major_formatter(date_format)
    fig.autofmt_xdate()
    fig.tight_layout()
    plt.show()

