import pandas as pd
import yfinance as yf
import argparse
import datetime


def calculate_price_movement(
    data_1day: pd.DataFrame, data_90day: pd.DataFrame
) -> tuple[float, float, float]:
    """
    Parameters:
        data_1day (pd.DataFrame): Price for ticker, every 1m for last 24h
        data_90day (pd.DataFrame): Price for ticker, every 1h for last 90days

    Returns:
        current_price (float): Current price
        change_1day (float): Percentage price change during last trading day
        change_7day (float): Percentage price change since last trading day >=7days ago
        change_30day (float): Percentage price change since last trading day >=30days ago
    """
    current_price = data_1day.iloc[-1, 3]
    datetime_30_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
    datetime_7_days_ago = datetime.datetime.now() - datetime.timedelta(days=7)

    finding_trading_day_data_30 = True
    while finding_trading_day_data_30:
        try:
            date_30_days_ago = datetime_30_days_ago.strftime("%Y-%m-%d")
            change_30day = (
                (current_price - data_90day.loc[date_30_days_ago, "Close"])
                / data_90day.loc[date_30_days_ago, "Close"]
                * 100
            )
            finding_trading_day_data_30 = False
        except KeyError:
            # no data because this day was not a trading day
            datetime_30_days_ago = datetime_30_days_ago - datetime.timedelta(days=1)

    finding_trading_day_data_7 = True
    while finding_trading_day_data_7:
        try:
            date_7_days_ago = datetime_7_days_ago.strftime("%Y-%m-%d")
            change_7day = (
                (current_price - data_90day.loc[date_7_days_ago, "Close"])
                / data_90day.loc[date_7_days_ago, "Close"]
                * 100
            )
            finding_trading_day_data_7 = False
        except KeyError:
            # no data because this day was not a trading day
            datetime_7_days_ago = datetime_7_days_ago - datetime.timedelta(days=1)

    change_1day = (current_price - data_1day.iloc[0, 0]) / data_1day.iloc[0, 0] * 100

    return current_price, change_1day, change_7day, change_30day


def main():
    # fetch ticker(s) argument from bash terminal command
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-portfolio", nargs="?", const="TSLA,AMZN,SNAP,COIN,BTC-USD"
    )  # const is default portfolio
    args = parser.parse_args()

    portfolio = args.portfolio.upper().split(",")

    for ticker in portfolio:
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
