import datetime
import pandas as pd
import yfinance


def calculate_price_movement(ticker: str) -> tuple[float, float, float]:
    """
    Parameters:
        ticker (str): Ticker of asset to investigate

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
    change_30day = calculate_price_percentage_change_over_n_days(
        30, current_price, data_90day
    )
    change_7day = calculate_price_percentage_change_over_n_days(
        7, current_price, data_90day
    )
    change_1day = (current_price - data_1day.iloc[0, 0]) / data_1day.iloc[0, 0] * 100

    return current_price, change_1day, change_7day, change_30day


def calculate_price_percentage_change_over_n_days(
    n: int, current_price: float, data_90day: pd.DataFrame
) -> float:
    datetime_n_days_ago = datetime.datetime.now() - datetime.timedelta(days=n)
    finding_trading_day_data_n = True
    while finding_trading_day_data_n:
        try:
            date_n_days_ago = datetime_n_days_ago.strftime("%Y-%m-%d")
            change_nday = (
                (current_price - data_90day.loc[date_n_days_ago, "Close"])
                / data_90day.loc[date_n_days_ago, "Close"]
                * 100
            )
            finding_trading_day_data_n = False
        except KeyError:
            # no data because this day was not a trading day
            datetime_n_days_ago = datetime_n_days_ago - datetime.timedelta(days=1)
    return change_nday
