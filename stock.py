import argparse
import sys

from shared import calculate_price_movement

parser = argparse.ArgumentParser()
parser.add_argument("-stocks")


def main(args: list = sys.argv[1:]):
    parsed_args = parser.parse_args(args)
    stocks = parsed_args.stocks.upper().split(",")

    for ticker in stocks:
        (
            current_price,
            percentage_change_1day,
            percentage_change_7day,
            percentage_change_30day,
        ) = calculate_price_movement(ticker)

        summary = f"{ticker} -- Current price: {current_price:.2f} -- Daily change: {percentage_change_1day:.2f}%, 7-day change: {percentage_change_7day:.2f}%, 30-day change: {percentage_change_30day:.2f}%"

        print(summary)


if __name__ == "__main__":
    main()
