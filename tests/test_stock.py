import responses
import freezegun
from tests.conftest import (
    example_yahoo_api_response_90day_aapl_2023_03_01,
    example_yahoo_api_response_1day_aapl_2023_03_01,
    example_yahoo_api_response_90day_tsla_2023_03_01,
    example_yahoo_api_response_1day_tsla_2023_03_01,
)
import stock


@freezegun.freeze_time("2023-03-01")
def test_stock_with_one_ticker(capsys, mocked_responses):
    mocked_responses.get(
        "https://query2.finance.yahoo.com/v8/finance/chart/AAPL",
        match=[
            responses.matchers.query_param_matcher(
                {
                    "range": "90d",
                    "interval": "1d",
                    "includePrePost": False,
                    "events": "div,splits,capitalGains",
                }
            )
        ],
        status=200,
        json=example_yahoo_api_response_90day_aapl_2023_03_01,
    )
    mocked_responses.get(
        "https://query2.finance.yahoo.com/v8/finance/chart/AAPL",
        match=[
            responses.matchers.query_param_matcher(
                {
                    "range": "1d",
                    "interval": "1m",
                    "includePrePost": False,
                    "events": "div,splits,capitalGains",
                }
            )
        ],
        status=200,
        json=example_yahoo_api_response_1day_aapl_2023_03_01,
    )

    stock.main(["-stocks", "aapl"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "AAPL -- Current price: 145.09 -- Daily change: -1.23%, 7-day change: -2.57%, 30-day change: 1.62%\n"
    )


@freezegun.freeze_time("2023-03-01")
def test_stock_with_two_tickers(capsys, mocked_responses):
    mocked_responses.get(
        "https://query2.finance.yahoo.com/v8/finance/chart/AAPL",
        match=[
            responses.matchers.query_param_matcher(
                {
                    "range": "90d",
                    "interval": "1d",
                    "includePrePost": False,
                    "events": "div,splits,capitalGains",
                }
            )
        ],
        status=200,
        json=example_yahoo_api_response_90day_aapl_2023_03_01,
    )
    mocked_responses.get(
        "https://query2.finance.yahoo.com/v8/finance/chart/AAPL",
        match=[
            responses.matchers.query_param_matcher(
                {
                    "range": "1d",
                    "interval": "1m",
                    "includePrePost": False,
                    "events": "div,splits,capitalGains",
                }
            )
        ],
        status=200,
        json=example_yahoo_api_response_1day_aapl_2023_03_01,
    )
    mocked_responses.get(
        "https://query2.finance.yahoo.com/v8/finance/chart/TSLA",
        match=[
            responses.matchers.query_param_matcher(
                {
                    "range": "90d",
                    "interval": "1d",
                    "includePrePost": False,
                    "events": "div,splits,capitalGains",
                }
            )
        ],
        status=200,
        json=example_yahoo_api_response_90day_tsla_2023_03_01,
    )
    mocked_responses.get(
        "https://query2.finance.yahoo.com/v8/finance/chart/TSLA",
        match=[
            responses.matchers.query_param_matcher(
                {
                    "range": "1d",
                    "interval": "1m",
                    "includePrePost": False,
                    "events": "div,splits,capitalGains",
                }
            )
        ],
        status=200,
        json=example_yahoo_api_response_1day_tsla_2023_03_01,
    )

    stock.main(["-stocks", "aapl,tsla"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "AAPL -- Current price: 145.09 -- Daily change: -1.23%, 7-day change: -2.57%, 30-day change: 1.62%\nTSLA -- Current price: 202.75 -- Daily change: -1.62%, 7-day change: 0.94%, 30-day change: 21.65%\n"
    )
