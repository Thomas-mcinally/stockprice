from datetime import datetime, date, timedelta
from typing import List, Tuple
import requests


def calculate_percentage_price_change_over_n_days(
    n: int, timestamps: List[int], closing_prices: List[int]
) -> float:
    date_n_days_ago = (datetime.utcnow() - timedelta(days=n)).date()

    index_of_trading_day = 0
    # timestamps ordered from earliest to latest
    while (
        index_of_trading_day + 2 < len(timestamps)
        and date.fromtimestamp(timestamps[index_of_trading_day + 1]) <= date_n_days_ago
    ):
        index_of_trading_day += 1

    price_on_last_trading_day_n_days_ago = closing_prices[index_of_trading_day]
    current_price = closing_prices[-1]
    percentage_price_change = (
        100
        * (current_price - price_on_last_trading_day_n_days_ago)
        / price_on_last_trading_day_n_days_ago
    )

    return percentage_price_change


def calculate_price_movement(ticker: str) -> Tuple[float, str, float, float, float]:
    """
    Parameters:
        ticker (str): Ticker of asset to investigate

    Returns:
        current_price (float): Current price
        currency (str): The currency of the price
        percentage_change_1day (float): Price change during last trading day
        percentage_change_7day (float): Price change since last trading day >=7days ago
        percentage_change_30day (float): Price change since last trading day >=30days ago
    """
    response = requests.get(
        f"https://query2.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=30d",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    if response.status_code == 404:
        raise ValueError(f"The ticker symbol {ticker} is not listed on yahoo finance.")
    response_body = response.json()
    currency = response_body["chart"]["result"][0]["meta"]["currency"]
    closing_prices = response_body["chart"]["result"][0]["indicators"]["quote"][0][
        "close"
    ]
    timestamps = response_body["chart"]["result"][0]["timestamp"]

    current_price = closing_prices[-1]
    percentage_change_30day = calculate_percentage_price_change_over_n_days(
        30, timestamps, closing_prices
    )
    percentage_change_7day = calculate_percentage_price_change_over_n_days(
        7, timestamps, closing_prices
    )
    percentage_change_1day = calculate_percentage_price_change_over_n_days(
        1, timestamps, closing_prices
    )

    return (
        current_price,
        currency,
        percentage_change_1day,
        percentage_change_7day,
        percentage_change_30day,
    )
