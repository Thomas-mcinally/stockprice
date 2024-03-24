from dataclasses import dataclass
import datetime
from typing import List

import requests


@dataclass
class TickerStatistics:
    ticker: str
    currency: str
    current_price: float
    percentage_change_1day: float
    percentage_change_7day: float
    percentage_change_30day: float


def calculate_percentage_price_change_over_n_days(
    n: int, timestamps: List[int], closing_prices: List[float]
) -> float:
    current_price: float = closing_prices[-1]
    price_n_days_ago: float

    now_timestamp = datetime.datetime.utcnow().timestamp()
    start_timestamp = now_timestamp - n * 24 * 60 * 60

    if timestamps[0] >= start_timestamp:
        breakpoint()
        raise ValueError(
            "Not enough data to calculate price change over the last n days"
        )

    i = 0
    while i < len(timestamps):
        if timestamps[i] >= start_timestamp:
            break
        i += 1

    price_n_days_ago = closing_prices[i - 1]
    percentage_change = 100 * (current_price - price_n_days_ago) / price_n_days_ago
    return percentage_change


def get_ticker_statistics(ticker: str) -> TickerStatistics:
    response = requests.get(
        f"https://query2.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=35d",
        headers={"User-Agent": "Mozilla/5.0"},
    )

    if response.status_code == 404:
        raise ValueError(f"The ticker symbol {ticker} is not listed on yahoo finance.")

    response_json = response.json()
    currency: str = response_json["chart"]["result"][0]["meta"]["currency"]
    closing_prices: list[float] = response_json["chart"]["result"][0]["indicators"][
        "quote"
    ][0]["close"]
    timestamps: list[StopIteration] = response_json["chart"]["result"][0]["timestamp"]

    current_price: float = closing_prices[-1]
    percentage_change_1day: float = calculate_percentage_price_change_over_n_days(
        1, timestamps, closing_prices
    )
    percentage_change_7day: float = calculate_percentage_price_change_over_n_days(
        7, timestamps, closing_prices
    )
    percentage_change_30day: float = calculate_percentage_price_change_over_n_days(
        30, timestamps, closing_prices
    )

    return TickerStatistics(
        ticker=ticker,
        currency=currency,
        current_price=current_price,
        percentage_change_1day=percentage_change_1day,
        percentage_change_7day=percentage_change_7day,
        percentage_change_30day=percentage_change_30day,
    )
