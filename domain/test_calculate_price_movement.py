import responses
from domain.conftest import example_yahoo_api_response_1day_tsla, example_yahoo_api_response_90day_tsla
from domain.calculate_price_movement import calculate_price_movement

def test_calculate_price_movement(mocked_responses):
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
        json=example_yahoo_api_response_90day_tsla,
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
        json=example_yahoo_api_response_1day_tsla,
    )

    current_price, change_1day, change_7day, change_30day = calculate_price_movement("tsla")
    expected_current_price, expected_change_1day, expected_change_7day, expected_change_30day  = 196.86, 0.27, -5.50, 10.66
    assert round(current_price, 2) == expected_current_price
    assert round(change_1day, 2) == expected_change_1day
    assert round(change_7day, 2) == expected_change_7day
    assert round(change_30day, 2) == expected_change_30day
