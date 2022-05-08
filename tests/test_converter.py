import pytest
from first_fast_api_app.converter import convert_currency, get_conversion_rate


def test_eur_czk():
    assert get_conversion_rate("EUR", "CZK") == 25


def test_convert_currency():
    assert convert_currency(2, "EUR", "CZK") == 50


@pytest.mark.parametrize("test_input,expected", [(2, 50), (3, 75), (5, 125)])
def test_convert_currency_with_param(test_input, expected):
    assert convert_currency(test_input, "EUR", "CZK") == expected
