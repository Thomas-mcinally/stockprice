import sys

from stockprice.calculate_price_movement import calculate_price_movement
from stockprice.errors import TimeZoneError


def main(args: list = sys.argv):
    raw_input = args[1]
    stocks = raw_input.upper().split(",")

    for ticker in stocks:
        try:
            (
                current_price,
                percentage_change_1day,
                percentage_change_7day,
                percentage_change_30day,
            ) = calculate_price_movement(ticker)
        except TimeZoneError:
            print(f"Something went wrong when processing {ticker} - Time zone error")
            return

        summary = f"{ticker} -- Current price: {current_price:.2f} -- Daily change: {percentage_change_1day:.2f}%, 7-day change: {percentage_change_7day:.2f}%, 30-day change: {percentage_change_30day:.2f}%"

        print(summary)


if __name__ == "__main__":
    main()
