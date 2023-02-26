import responses
from domain.conftest import example_api_response_1day, example_api_response_90day
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
        json=example_api_response_90day,
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
        json=example_api_response_1day,
    )

    calculate_price_movement("tsla")
