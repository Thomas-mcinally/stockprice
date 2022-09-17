A set of unix-terminal tools for personal finance

- The tools utilize the Yahoo Finance API
- Work for all tickers listed on Yahoo Finance, including cryptocurrency trading pairs (e.g. TSLA, AAPL, BTC-USD, ETH-USD) 
- Works for terminals running unix shells (e.g. Bash, Zsh)


# Stock_overview.py

**Input:** One-line command in terminal (info TICKER)

![](images/input_stock_overview.GIF)

**Output:** Pop-out matplotlib window with historic price movement and trading volumes for that ticker

![](images/output_stock_overview.GIF)


# Portfolio.py

**Input:** One-line command in terminal  (portfolio LIST,OF,TICKERS)

![](images/input_portfolio.GIF)

**Output:** Returns daily change, 7-day change and 30-day change for all tickers

![](images/output_portfolio.GIF)

## Steps to setup locally 
1. Clone this repository
2. `pipenv install` in this directory
3. `./install.sh` in this directory
