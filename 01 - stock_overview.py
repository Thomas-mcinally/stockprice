import pandas as pd
import yfinance as yf
from mplfinance import figure, plot, show
import argparse
import datetime


def calculate_price_movement(
    ticker: str, data_1day: pd.DataFrame, data_90day: pd.DataFrame
) -> tuple[float, float, float, float]:
    """
    Parameters:
        data_1day (pd.DataFrame): Price for ticker, every 30m for last 24h
        data_90day (pd.DataFrame): Price for ticker evert 1h for last 90days

    Returns:
        current_price (float): Current price for ticker
        change_1day (float): Percentage price change over last 24hr
        change_7day (float): Percentage price change over last 7days
        change_30day (float): Percentage price change over last 30days
    """
    current_price = data_1day.iloc[-1, 3]

    date_30_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)
    date_7_days_ago = datetime.datetime.now() - datetime.timedelta(days=7)

    # normal stock market closed on saturdays & sundays
    if "-" not in ticker:  # cryptocurrency tickers contain '-', e.g. BTC-USD
        if date_30_days_ago.weekday() == 6:
            date_30_days_ago = date_30_days_ago - datetime.timedelta(days=2)
        elif date_30_days_ago.weekday() == 5:
            date_30_days_ago = date_30_days_ago - datetime.timedelta(days=1)

        if date_7_days_ago.weekday() == 6:
            date_7_days_ago = date_7_days_ago - datetime.timedelta(days=2)
        elif date_7_days_ago.weekday() == 5:
            date_7_days_ago = date_7_days_ago - datetime.timedelta(days=1)

    date_30_days_ago = date_30_days_ago.strftime("%Y-%m-%d")
    date_7_days_ago = date_7_days_ago.strftime("%Y-%m-%d")

    change_30day = (
        (current_price - data_90day.loc[date_30_days_ago, "Close"])
        / data_90day.loc[date_30_days_ago, "Close"]
        * 100
    )
    change_7day = (
        (current_price - data_90day.loc[date_7_days_ago, "Close"])
        / data_90day.loc[date_7_days_ago, "Close"]
        * 100
    )

    change_1day = (current_price - data_1day.iloc[0, 0]) / data_1day.iloc[0, 0] * 100

    return current_price, change_1day, change_7day, change_30day


def visualize_results(
    ticker: str,
    data_1day: pd.DataFrame,
    data_90day: pd.DataFrame,
    current_price: float,
    change_1day: float,
    change_7day: float,
    change_30day: float,
) -> figure:
    """
    Parameters:
        ticker (str): Stock ticker
        data_1day (pd.DataFrame): Price for ticker every 30m for last 24h
        data_90day (pd.DataFrame): Price for ticker evert 1h for last 90days
        current_price (float): Current price for ticker
        change_1day (float): Percentage price change over last 24hr
        change_7day (float): Percentage price change over last 7days
        change_30day (float): Percentage price change over last 30days

    Returns:
        fig (figure): Matplotlib finance figure containing 90day line plot and 24hr candle stick plot of price movement
    """
    last_trading_day = data_1day.index.format()[0].split(" ")[0]

    fig = figure(figsize=(13, 6), style="blueskies")

    ax1 = fig.add_subplot(2, 2, 1)
    ax1_vol = fig.add_subplot(2, 2, 3)
    ax2 = fig.add_subplot(2, 2, 2)
    ax2_vol = fig.add_subplot(2, 2, 4)

    plot(
        data_90day,
        ax=ax1,
        volume=ax1_vol,
        type="line",
        datetime_format="%d-%m",
        xrotation=20,
        axtitle=ticker + " last 90 days",
    )
    plot(
        data_1day,
        ax=ax2,
        volume=ax2_vol,
        type="candle",
        xrotation=20,
        axtitle=ticker + " last trading day (" + last_trading_day + ")",
    )
    fig.suptitle(
        "Current market price: "
        + "%.2f" % current_price
        + " , Daily change: "
        + "%.2f" % change_1day
        + "%"
        + " , 7-day change: "
        + "%.2f" % change_7day
        + "%"
        + " , 30-day change: "
        + "%.2f" % change_30day
        + "%"
    )

    return fig


def main():
    # fetch ticker argument from bash terminal command
    parser = argparse.ArgumentParser()
    parser.add_argument("-ticker")
    args = parser.parse_args()
    ticker = args.ticker
    ticker = ticker.upper()

    data_1day = yf.download(
        ticker, period="1d", interval="30m", auto_adjust=True, progress=False
    )
    data_90day = yf.download(
        ticker, period="90d", interval="1d", auto_adjust=True, progress=False
    )

    current_price, change_1day, change_7day, change_30day = calculate_price_movement(
        ticker, data_1day, data_90day
    )

    fig = visualize_results(
        ticker,
        data_1day,
        data_90day,
        current_price,
        change_1day,
        change_7day,
        change_30day,
    )
    show()


if __name__ == "__main__":
    main()
