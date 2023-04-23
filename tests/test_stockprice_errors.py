import freezegun
from stockprice.main import main
from tests.conftest import example_yahoo_api_response_30day_tsla_2023_03_13


def test_ticker_not_listed_on_yahoo_finance_one_ticker(
    capsys, mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "MSF",
        {
            "chart": {
                "result": None,
                "error": {
                    "code": "Not Found",
                    "description": "No data found, symbol may be delisted",
                },
            }
        },
        404,
    )

    main(["~/stockprice", "msf"])

    stdout = capsys.readouterr().out
    assert stdout == "The ticker symbol MSF is not listed on yahoo finance.\n"


@freezegun.freeze_time("2023-03-13")
def test_ticker_not_listed_on_yahoo_finance_multiple_tickers(
    capsys, mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "XF",
        {
            "chart": {
                "result": None,
                "error": {
                    "code": "Not Found",
                    "description": "No data found, symbol may be delisted",
                },
            }
        },
        404,
    )
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "TSLA", example_yahoo_api_response_30day_tsla_2023_03_13
    )

    main(["~/bin/stockprice", "xf,tsla"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "The ticker symbol XF is not listed on yahoo finance.\nTSLA -- Current price: 174.95 USD -- Daily change: 0.87%, 7-day change: -9.73%, 30-day change: -11.14%\n"
    )


def test_stockprice_with_no_tickers(capsys):

    main(["~/home/stockprice"])

    stdout = capsys.readouterr().out
    assert (
        stdout
        == "Please provide at least one stock ticker.\nExample: stockprice tsla,aapl\n"
    )
