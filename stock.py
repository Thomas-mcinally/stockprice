import argparse

from shared import calculate_price_movement


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-stocks", nargs="?", const="TSLA,AMZN,SNAP,COIN,BTC-USD"
    )  # const is default argument
    args = parser.parse_args()

    stocks = args.stocks.upper().split(",")

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
