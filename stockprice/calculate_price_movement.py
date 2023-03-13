import datetime
from typing import List, Tuple
import requests

def new_calculate_percentage_price_change_over_n_days(n, timestamps:List[int], closing_prices: List[int]):
    datetime_n_days_ago = datetime.datetime.now() - datetime.timedelta(days=n)
    date_n_days_ago = datetime_n_days_ago.date()

    index_of_price = None
    for index in range(len(timestamps)):
        past_date = datetime.datetime.fromtimestamp(timestamps[index]).date()
        if past_date > date_n_days_ago:
            break
        index_of_price = index

    price_n_days_ago = closing_prices[index_of_price]
    current_price = closing_prices[-1]
    return 100 * (current_price - price_n_days_ago) / price_n_days_ago 


def calculate_price_movement(ticker: str) -> Tuple[float, float, float]:
    """
    Parameters:
        ticker (str): Ticker of asset to investigate

    Returns:
        current_price (float): Current price
        percentage_change_1day (float): Price change during last trading day
        percentage_change_7day (float): Price change since last trading day >=7days ago
        percentage_change_30day (float): Price change since last trading day >=30days ago
    """
    response = requests.get(
        f"https://query2.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=30d",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    closing_prices = response.json()["chart"]["result"][0]["indicators"]["quote"][0]["close"]
    timestamps = response.json()["chart"]["result"][0]["timestamp"]
    current_price = closing_prices[-1]


    percentage_change_30day = new_calculate_percentage_price_change_over_n_days(30, timestamps,closing_prices)
    percentage_change_7day = new_calculate_percentage_price_change_over_n_days(7, timestamps,closing_prices)
    percentage_change_1day = new_calculate_percentage_price_change_over_n_days(1, timestamps,closing_prices)

    return (current_price,percentage_change_1day,percentage_change_7day,percentage_change_30day)
