'''
Thomas McInally 11/02/2022

This module will allow you easily get market data for most stocks/cryptocurrencies with a single command in terminal

How to use:
If we want an overview for tesla stock, simply type 'info TSLA' in terminal
This should bring up a figure containing:
1. Current market price and daily % change
2. Line plot for last 90 day price movement
3. Candlestick plot for last 24hr price movement

How to setup (for git bash):
1. Download this module and place it in a directory accessible by your terminal
2. In the home directory for git bash, create the alias by adding the following line to your .bashrc:
        alias info='cd /c/Users/Bruker/desktop/projects/terminal_finance && python stock_overview.py -ticker'
   This alias will allow you to call this stock_overview.py and pass an argument to it with a single terminal command


TODO:
1. Improve accuracy of 7-day and 30-day % change by using hourly instead of daily data for closing price 
        A bit difficult because need to:
         a) round off current datetime to closest half hour, use   rounded = now - (now - datetime.min) % timedelta(minutes=30)
         b) If stock market closed, round of to previous 15:30
         c) account for my time zone being different than stock's time zone
2. Make current price more accurate (currently 30 min lag)
    Can use .info method, but need to make sure it doesnt slow down program significantly
'''


#Import required packages
import yfinance as yf
from mplfinance import figure, plot, show
from argparse import ArgumentParser
from datetime import datetime, timedelta



def overview(ticker:str) -> figure:
    '''
    Downloads and calculates key metrics about ticker, and combined them into a nice figure

            Parameters:
                ticker(str): The yahoo finance ticker for the asset (e.g. TSLA or BTC-USD)
            
            Returns:
                fig : Matplotlib finance figure containing 90day line plot and 24hr candle stick plot of price movement
    '''

    data_90days = yf.download(ticker, period='90d',interval='1d', auto_adjust=True, progress=False)
    data_1day = yf.download(ticker, period='1d',interval='30m', auto_adjust=True, progress=False)

    current_price = data_1day.iloc[-1,3]  #30 min delay in updating current price
    
    last_trading_day=data_1day.index.format()[0].split(' ')[0]
    date_30_days_ago=datetime.now()-timedelta(days=30)
    date_7_days_ago=datetime.now()-timedelta(days=7)

    #for stocks, change date_30_days_ago and date_7_days_ago to previous friday if it is a sunday or saturday
    #stock closed on saturdays & sundays
    if '-' not in ticker: #cryptocurrency tickers contain '-', e.g. BTC-USD
        if date_30_days_ago.weekday() == 6:
            date_30_days_ago = date_30_days_ago - timedelta(days=2)
        elif date_30_days_ago.weekday() == 5:
            date_30_days_ago = date_30_days_ago - timedelta(days=1)

        if date_7_days_ago.weekday() == 6:
            date_7_days_ago = date_7_days_ago - timedelta(days=2)
        elif date_7_days_ago.weekday() == 5:
            date_7_days_ago = date_7_days_ago - timedelta(days=1)

    date_30_days_ago=date_30_days_ago.strftime('%Y-%m-%d')
    date_7_days_ago=date_7_days_ago.strftime('%Y-%m-%d')

    
    #find 30-day and 7-day return
    day_30_return=(current_price-data_90days.loc[date_30_days_ago,'Close'])/data_90days.loc[date_30_days_ago,'Close']*100
    day_7_return=(current_price-data_90days.loc[date_7_days_ago,'Close'])/data_90days.loc[date_7_days_ago,'Close']*100

    #find daily return (change in from start to end of latest trading day)
    daily_return = (current_price-data_1day.iloc[0,0])/data_1day.iloc[0,0]*100



    fig = figure(figsize=(13,6), style='blueskies')

    ax1=fig.add_subplot(2,2,1)
    ax1_vol=fig.add_subplot(2,2,3)
    ax2=fig.add_subplot(2,2,2)
    ax2_vol=fig.add_subplot(2,2,4)

    plot(data_90days, ax=ax1, volume=ax1_vol, type='line', datetime_format='%d-%m',xrotation=20, axtitle=ticker + ' last 90 days')
    plot(data_1day, ax=ax2, volume=ax2_vol, type='candle',xrotation=20, axtitle=ticker + ' last trading day ('+last_trading_day+')')
    fig.suptitle('Current market price: ' + '%.2f' % current_price +' , Daily change: ' + '%.2f' % daily_return +'%'+' , 7-day change: ' + '%.2f' % day_7_return +'%'+' , 30-day change: ' + '%.2f' % day_30_return +'%')
    
    return fig


#code to enable passing argument at the same time .py file is called in command line
parser = ArgumentParser()
parser.add_argument("-ticker")
args = parser.parse_args()
ticker = args.ticker



#Run
ticker=ticker.upper() #make ticker all upper case 

fig = overview(ticker)
show() #display fig


