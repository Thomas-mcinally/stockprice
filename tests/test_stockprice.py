import freezegun
import pytest
from tests.conftest import (
    example_yahoo_api_response_30day_tsla_2023_03_13,
    example_yahoo_api_response_30day_aapl_2023_03_13,
    example_yahoo_api_response_30day_btc_eur_2023_03_13,
    example_yahoo_api_response_30day_tsla_2023_03_14_before_market_open,
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
        == "TSLA -- Current price: 174.95 USD -- Daily change: 0.87%, 7-day change: -9.73%, 30-day change: -11.14%\n"
    )


@freezegun.freeze_time("2023-03-14")
def test_stockprice_with_one_ticker_before_market_opens(
    capsys, mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "TSLA", example_yahoo_api_response_30day_tsla_2023_03_14_before_market_open
    )

    main(["stockprice", "tsla"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "TSLA -- Current price: 174.95 USD -- Daily change: 0.87%, 7-day change: -6.80%, 30-day change: -11.14%\n"
    )


@freezegun.freeze_time("2023-03-13")
def test_stockprice_with_one_ticker_crypto(
    capsys, mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "BTC-EUR", example_yahoo_api_response_30day_btc_eur_2023_03_13
    )

    main(["stockprice", "btc-eur"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "BTC-EUR -- Current price: 24295.92 EUR -- Daily change: 9.62%, 7-day change: 8.32%, 30-day change: 11.51%\n"
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
        == "TSLA -- Current price: 174.95 USD -- Daily change: 0.87%, 7-day change: -9.73%, 30-day change: -11.14%\nAAPL -- Current price: 150.47 USD -- Daily change: 1.33%, 7-day change: -2.18%, 30-day change: -0.36%\n"
    )


@freezegun.freeze_time("2023-03-13")
def test_stockprice_with_whitespace(
    capsys, mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "TSLA", example_yahoo_api_response_30day_tsla_2023_03_13
    )
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "AAPL", example_yahoo_api_response_30day_aapl_2023_03_13
    )

    main(["stockprice", "tsla,", "aapl"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "TSLA -- Current price: 174.95 USD -- Daily change: 0.87%, 7-day change: -9.73%, 30-day change: -11.14%\nAAPL -- Current price: 150.47 USD -- Daily change: 1.33%, 7-day change: -2.18%, 30-day change: -0.36%\n"
    )


@pytest.mark.parametrize(
    "input_sys_argv", [["stockprice", "tsla,aapl,"], ["stockprice", "tsla,", "aapl,"]]
)
@freezegun.freeze_time("2023-03-13")
def test_stockprice_trailing_comma(
    capsys, mock_GET_yahoo_v8_finance_chart_api_30day_range, input_sys_argv
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "TSLA", example_yahoo_api_response_30day_tsla_2023_03_13
    )
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "AAPL", example_yahoo_api_response_30day_aapl_2023_03_13
    )

    main(input_sys_argv)

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "TSLA -- Current price: 174.95 USD -- Daily change: 0.87%, 7-day change: -9.73%, 30-day change: -11.14%\nAAPL -- Current price: 150.47 USD -- Daily change: 1.33%, 7-day change: -2.18%, 30-day change: -0.36%\n"
    )
