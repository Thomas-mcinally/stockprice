import sys

from stockprice.get_ticker_statistics import TickerStatistics, get_ticker_statistics


def main(args: list = sys.argv) -> None:
    if len(args) == 1:
        print("Please provide at least one stock ticker.")
        print("Example: stockprice tsla,aapl")
        return
    raw_inputs = args[1:]
    stock_tickers = []
    for input in raw_inputs:
        input = input.upper()
        if input[-1] == ",":
            input = input[:-1]

        stock_tickers.extend(input.split(","))
    for ticker in stock_tickers:
        try:
            statistics: TickerStatistics = get_ticker_statistics(ticker)
            summary = f"{statistics.ticker} -- Current price: {statistics.current_price:.2f} {statistics.currency} -- Daily change: {statistics.percentage_change_1day:.2f}%, 7-day change: {statistics.percentage_change_7day:.2f}%, 30-day change: {statistics.percentage_change_30day:.2f}%"
            print(summary)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
