import sys

from stockprice.calculate_price_movement import calculate_price_movement


def main(args: list = sys.argv) -> None:
    raw_inputs = args[1:]
    stock_tickers = []
    for input in raw_inputs:
        input = input.upper()
        if input[-1] == ",":
            input = input[:-1]

        stock_tickers.extend(input.split(","))
    for ticker in stock_tickers:
        try:
            (
                current_price,
                currency,
                percentage_change_1day,
                percentage_change_7day,
                percentage_change_30day,
            ) = calculate_price_movement(ticker)
            summary = f"{ticker} -- Current price: {current_price:.2f} {currency} -- Daily change: {percentage_change_1day:.2f}%, 7-day change: {percentage_change_7day:.2f}%, 30-day change: {percentage_change_30day:.2f}%"

            print(summary)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
