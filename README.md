# stockprice

CLI tool to check historic price movement of stock tickers
- Work for all tickers listed on Yahoo Finance, including cryptocurrency trading pairs (e.g. TSLA, AAPL, BTC-USD, ETH-USD)

**Input:** One-line command in terminal  (stockprice LIST,OF,TICKERS)

![](images/input_stockprice.png)

**Output:** Returns daily change, 7-day change and 30-day change for all tickers

![](images/output_stockprice.png)

## Installation
Using [pipx](https://pypa.github.io/pipx/)
```
pipx install stockprice-cli
```

Alternatively, using pip (or pip3):
```
pip install stockprice-cli
```
