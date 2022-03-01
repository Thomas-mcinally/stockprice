'''
Thomas McInally 11/02/2022

This module allows you to eaily view recent price data for a list of yahoo finance stock tickers, with a single command in terminal

How to use:
1. To get info on stocks in default portfolio, simply execute the command 'portfolio' in terminal
2. To specify which stocks to show info for (e.g. TSLA and SNAP), execute the command 'portfolio TSLA,SNAP' in terminal

To update the default portfolio, edit 'const' in the add_argument method

How to setup (for git bash):
1. Download this module and place it in a directory accessible by your terminal
2. In the home directory for git bash, create the alias by adding the following line to your .bashrc:
        alias portfolio='cd /c/Users/Bruker/Documents/GitHub/finance && python portfolio.py -portfolio'
   This alias will allow you to call portfolio.py and pass an argument to it with a single terminal command
'''




#Import required packages
import yfinance as yf
import argparse
from datetime import datetime, timedelta



def ticker_summary(ticker:str) -> str:
    '''
    Get summary of recent price movement for yahoo finance ticker

            Parameters:
                ticker (str): Yahoo finance ticker (e.g. TSLA or BTC-USD)

            Returns:
                price movement (str): A string containing daily, 7-day and 30-day price movement for the ticker
    '''


    data_90days = yf.download(ticker, period='90d',interval='1d', auto_adjust=True, progress=False)
    data_1day = yf.download(ticker, period='1d',interval='1m', auto_adjust=True, progress=False)
    current_price = data_1day.iloc[-1,3] #1 min delay
    #find date 30 & 7 days ago to extract price from data_90days
    date_30_days_ago=datetime.now()-timedelta(days=30)
    date_7_days_ago=datetime.now()-timedelta(days=7)
    #for stocks, change date_30_days_ago and date_7_days_ago to previous friday if it is a sunday or saturday
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
    #find daily return
    daily_return = (current_price - data_1day.iloc[0,0])/data_1day.iloc[0,0]*100
    return(ticker + ' Daily change:' + '%.2f' % daily_return +'%'+' , 7-day change:' + '%.2f' % day_7_return +'%'+' , 30-day change:' + '%.2f' % day_30_return +'%')




#code to enable passing argument at the same time .py file is called in command line
parser = argparse.ArgumentParser()
parser.add_argument('-portfolio', nargs='?', const='TSLA,AMZN,COIN,SNAP') #const is default portfolio
args = parser.parse_args()


portfolio = args.portfolio.upper().split(',') #list of stock tickers

for ticker in portfolio:
    summary = ticker_summary(ticker)
    print(summary)





