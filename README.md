A set of terminal tools for personal finance

- The tools utilize the Yahoo Finance API
- Work for all tickers listed on Yahoo Finance, including cryptocurrency trading pairs (e.g. TSLA, AAPL, BTC-USD, ETH-USD) 
- Works for terminals running unix shells (e.g. Bash, Zsh)


# Stockplot.py

**Input:** One-line command in terminal (stockplot TICKER)

![](images/input_stockplot.png)

**Output:** Pop-out matplotlib window with historic price movement and trading volumes for that ticker

![](images/output_stockplot.png)


# Stock.py

**Input:** One-line command in terminal  (stock LIST,OF,TICKERS)

![](images/input_stock.png)

**Output:** Returns daily change, 7-day change and 30-day change for all tickers

![](images/output_stock.png)

## Steps to setup locally 
Before running the commands below, make sure `pipenv` is installed
1. Clone this repository
2. `pipenv install` in this directory
3. `./install.sh` in this directory
