import freezegun
from tests.conftest import (
    example_yahoo_api_response_90day_aapl_2023_03_01,
    example_yahoo_api_response_1day_aapl_2023_03_01,
    example_yahoo_api_response_90day_tsla_2023_03_01,
    example_yahoo_api_response_1day_tsla_2023_03_01,
)
from stockprice.main import main


@freezegun.freeze_time("2023-03-01")
def test_stockprice_with_one_ticker(
    capsys,
    mock_GET_yahoo_v8_finance_chart_api_1day_range,
    mock_GET_yahoo_v8_finance_chart_api_90day_range,
):
    mock_GET_yahoo_v8_finance_chart_api_90day_range(
        "AAPL", example_yahoo_api_response_90day_aapl_2023_03_01
    )
    mock_GET_yahoo_v8_finance_chart_api_1day_range(
        "AAPL", example_yahoo_api_response_1day_aapl_2023_03_01
    )

    main(["stockprice", "aapl"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "AAPL -- Current price: 145.09 -- Daily change: -1.23%, 7-day change: -2.57%, 30-day change: 1.62%\n"
    )


@freezegun.freeze_time("2023-03-01")
def test_stockprice_with_two_tickers(
    capsys,
    mock_GET_yahoo_v8_finance_chart_api_1day_range,
    mock_GET_yahoo_v8_finance_chart_api_90day_range,
):
    mock_GET_yahoo_v8_finance_chart_api_90day_range
    mock_GET_yahoo_v8_finance_chart_api_90day_range(
        "AAPL", example_yahoo_api_response_90day_aapl_2023_03_01
    )
    mock_GET_yahoo_v8_finance_chart_api_1day_range(
        "AAPL", example_yahoo_api_response_1day_aapl_2023_03_01
    )
    mock_GET_yahoo_v8_finance_chart_api_90day_range(
        "TSLA", example_yahoo_api_response_90day_tsla_2023_03_01
    )
    mock_GET_yahoo_v8_finance_chart_api_1day_range(
        "TSLA", example_yahoo_api_response_1day_tsla_2023_03_01
    )

    main(["stockprice", "aapl,tsla"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "AAPL -- Current price: 145.09 -- Daily change: -1.23%, 7-day change: -2.57%, 30-day change: 1.62%\nTSLA -- Current price: 202.75 -- Daily change: -1.62%, 7-day change: 0.94%, 30-day change: 21.65%\n"
    )
