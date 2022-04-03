import yfinance as yf
import argparse
import datetime
from pandas import DataFrame


def calculate_price_movement(ticker:str, data_1day:DataFrame, data_90day:DataFrame) -> tuple((float,float,float,float)):
    '''
    Parameters:
        data_1day (DataFrame) - Price for ticker, every 30m for last 24h
        data_90day (DataFrame) - Price for ticker evert 1h for last 90days
        
    Returns:
        current_price (float) - Current price for ticker
        change_1day (float) - Percentage price change over last 24hr
        change_7day (float) - Percentage price change over last 7days
        change_30day (float) - Percentage price change over last 30days
    '''
    current_price = data_1day.iloc[-1,3]  #30 min delay in updating current price
    
    date_30_days_ago=datetime.datetime.now()-datetime.timedelta(days=30)
    date_7_days_ago=datetime.datetime.now()-datetime.timedelta(days=7)

    #for stocks, change date_30_days_ago and date_7_days_ago to previous friday if it is a sunday or saturday
    #stock closed on saturdays & sundays
    if '-' not in ticker: #cryptocurrency tickers contain '-', e.g. BTC-USD
        if date_30_days_ago.weekday() == 6:
            date_30_days_ago = date_30_days_ago - datetime.timedelta(days=2)
        elif date_30_days_ago.weekday() == 5:
            date_30_days_ago = date_30_days_ago - datetime.timedelta(days=1)

        if date_7_days_ago.weekday() == 6:
            date_7_days_ago = date_7_days_ago - datetime.timedelta(days=2)
        elif date_7_days_ago.weekday() == 5:
            date_7_days_ago = date_7_days_ago - datetime.timedelta(days=1)

    date_30_days_ago=date_30_days_ago.strftime('%Y-%m-%d')
    date_7_days_ago=date_7_days_ago.strftime('%Y-%m-%d')

    
    #find 30-day and 7-day return
    change_30day=(current_price-data_90day.loc[date_30_days_ago,'Close'])/data_90day.loc[date_30_days_ago,'Close']*100
    change_7day=(current_price-data_90day.loc[date_7_days_ago,'Close'])/data_90day.loc[date_7_days_ago,'Close']*100

    #find daily return (change in from start to end of latest trading day)
    change_1day = (current_price-data_1day.iloc[0,0])/data_1day.iloc[0,0]*100

    return change_1day, change_7day, change_30day


def main():
    #fetch ticker(s) argument from bash terminal command
    parser = argparse.ArgumentParser()
    parser.add_argument('-portfolio', nargs='?', const='TSLA,AMZN,COIN,SNAP') #const is default portfolio
    args = parser.parse_args()

    #split input argument into list of stock tickers
    portfolio = args.portfolio.upper().split(',') 

    #calculate historic price change for each ticker
    for ticker in portfolio:
        data_90day = yf.download(ticker, period='90d',interval='1d', auto_adjust=True, progress=False)
        data_1day = yf.download(ticker, period='1d',interval='1m', auto_adjust=True, progress=False)
        
        change_1day, change_7day, change_30day = calculate_price_movement(ticker, data_1day, data_90day)

        
        summary = (ticker + ' Daily change:' + '%.2f' % change_1day +'%'+' , 7-day change:' + '%.2f' % change_7day +'%'+' , 30-day change:' + '%.2f' % change_30day +'%')

        print(summary)

if __name__ == '__main__':
    main()






