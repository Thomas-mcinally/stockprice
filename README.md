A set of bash-terminal tools for personal finance

- The tools utilize the Yahoo Finance API
- Work for all tickers listed on Yahoo Finance, including cryptocurrency trading pairs (e.g. TSLA, AAPL, BTC-USD, ETH-USD) 


# Stock_overview.py

**Input:** One-line command in bash terminal (info TICKER)

![](images/input_stock_overview.GIF)

**Output:** Pop-out matplotlib window with historic price movement and trading volumes for that ticker

![](images/output_stock_overview.GIF)

## Steps to run locally 
1. Download this module and place it in a directory accessible by your bash terminal
2. Add the following line to your .bashrc:  alias info='cd /c/PATH/TO/DIRECTORY/WITH/MODULE && python stock_overview.py -ticker'


# Portfolio.py

**Input:** One-line command in bash terminal  (portfolio LIST,OF,TICKERS)

![](images/input_portfolio.GIF)

**Output:** Returns daily change, 7-day change and 30-day change for all tickers

![](images/output_portfolio.GIF)

## Steps to run locally 
1. Download this module and place it in a directory accessible by your bash terminal
2. Add the following line to your .bashrc:  alias portfolio='cd /c/PATH/TO/DIRECTORY/WITH/MODULE && python portfolio.py -portfolio'
