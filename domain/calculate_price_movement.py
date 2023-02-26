import datetime
import pandas as pd
import yfinance


def calculate_price_movement(
    ticker: str
) -> tuple[float, float, float]:
    """
    Parameters:
        ticker (str): Ticker of asset to find investigate

    Returns:
        current_price (float): Current price
        change_1day (float): Percentage price change during last trading day
        change_7day (float): Percentage price change since last trading day >=7days ago
        change_30day (float): Percentage price change since last trading day >=30days ago
    """
    data_90day: pd.DataFrame = yfinance.download(
            ticker, period="90d", interval="1d", auto_adjust=True, progress=False
        )
    data_1day: pd.DataFrame = yfinance.download(
        ticker, period="1d", interval="1m", auto_adjust=True, progress=False
    )
    

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
