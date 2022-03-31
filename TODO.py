#stock_overview.py
'''
1. Improve accuracy of 7-day and 30-day % change by using hourly instead of daily data for closing price 
        A bit difficult because need to:
         a) round off current datetime to closest half hour, use   rounded = now - (now - datetime.min) % timedelta(minutes=30)
         b) If stock market closed, round of to previous 15:30
         c) account for my time zone being different than stock's time zone
2. Make current price more accurate (currently 30 min lag)
    Can use .info method, but need to make sure it doesnt slow down program significantly
'''