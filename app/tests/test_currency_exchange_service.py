import pytest
from app.services import CurrencyExchangeService
from app.main import rates

exchange_service = CurrencyExchangeService(rates)

def test_convert_valid():
    assert exchange_service.convert("USD", "JPY", "1,525") == "170,496.53"
    assert exchange_service.convert("TWD", "USD", "1,000") == "32.81"
    assert exchange_service.convert("JPY", "TWD", "10,000") == "2,695.60"

def test_unsupported_currency():
    with pytest.raises(ValueError):
        exchange_service.convert("USD", "EUR", "100")
        exchange_service.convert("EUR", "USD", "100")

def test_invalid_amount():
    with pytest.raises(ValueError):
        exchange_service.convert("USD", "JPY", "abc")
        exchange_service.convert("USD", "JPY", "0!e4")

def test_rounding():
    assert exchange_service.convert("USD", "JPY", "1,000.56") == "111,863.61"
    assert exchange_service.convert("USD", "JPY", "1,000.555") == "111,863.61"
    assert exchange_service.convert("USD", "JPY", "1,000.554") == "111,862.49"
    assert exchange_service.convert("USD", "JPY", "1,000.55") == "111,862.49"
    assert exchange_service.convert("USD", "JPY", "1,000.5") == "111,856.90"
    assert exchange_service.convert("USD", "JPY", "1,000") == "111,801.00"
