import freezegun
from tests.conftest import (
    example_yahoo_api_response_30day_tsla_2023_03_13,
    example_yahoo_api_response_30day_aapl_2023_03_13,
    example_yahoo_api_response_30day_btc_usd_2023_03_13,
)
from stockprice.main import main


@freezegun.freeze_time("2023-03-13")
def test_stockprice_with_one_ticker(
    capsys, mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "TSLA", example_yahoo_api_response_30day_tsla_2023_03_13
    )

    main(["stockprice", "tsla"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "TSLA -- Current price: 174.95 -- Daily change: 0.87%, 7-day change: -9.73%, 30-day change: -11.14%\n"
    )


@freezegun.freeze_time("2023-03-13")
def test_stockprice_with_one_ticker_crypto(
    capsys, mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "BTC-USD", example_yahoo_api_response_30day_btc_usd_2023_03_13
    )

    main(["stockprice", "btc-usd"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "BTC-USD -- Current price: 24295.92 -- Daily change: 9.62%, 7-day change: 8.32%, 30-day change: 11.51%\n"
    )


@freezegun.freeze_time("2023-03-13")
def test_stockprice_with_two_tickers(
    capsys, mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "TSLA", example_yahoo_api_response_30day_tsla_2023_03_13
    )
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "AAPL", example_yahoo_api_response_30day_aapl_2023_03_13
    )

    main(["stockprice", "tsla,aapl"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "TSLA -- Current price: 174.95 -- Daily change: 0.87%, 7-day change: -9.73%, 30-day change: -11.14%\nAAPL -- Current price: 150.47 -- Daily change: 1.33%, 7-day change: -2.18%, 30-day change: -0.36%\n"
    )
