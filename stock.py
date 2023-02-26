import yfinance as yf
import argparse

from domain.calculate_price_movement import calculate_price_movement


def main():
    # fetch ticker(s) argument from bash terminal command
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-stocks", nargs="?", const="TSLA,AMZN,SNAP,COIN,BTC-USD"
    )  # const is default stocks
    args = parser.parse_args()

    stocks = args.stocks.upper().split(",")

    for ticker in stocks:
        data_90day = yf.download(
            ticker, period="90d", interval="1d", auto_adjust=True, progress=False
        )
        data_1day = yf.download(
            ticker, period="1d", interval="1m", auto_adjust=True, progress=False
        )

        (
            current_price,
            change_1day,
            change_7day,
            change_30day,
        ) = calculate_price_movement(data_1day, data_90day)

        summary = (
            ticker
            + f" -- Current price: {current_price:.2f} -- "
            + f"Daily change: {change_1day:.2f}%"
            + f", 7-day change: {change_7day:.2f}%"
            + f", 30-day change: {change_30day:.2f}%"
        )

        print(summary)


if __name__ == "__main__":
    main()
