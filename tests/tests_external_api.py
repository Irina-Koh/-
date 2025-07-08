from unittest.mock import patch
from src.external_api import convert_to_rub

def test_exchange_currency_1():
    """Тестирование функции exchange_currency() если валюта (currency) в
    транзакции в рублях"""
    trans = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    result = convert_to_rub(trans)
    assert result == 31957.58


@patch("requests.get")
def test_exchange_currency_2(mock_get):
    """Тестирование функции exchange_currency() если валюта (currency) в транзакции
    не в рублях и нужна конвертация"""
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 8221.37},
        "info": {"timestamp": 1748779696, "rate": 77.180757},
        "date": "2025-06-01",
        "result": 634531.560177,
    }

    result1 = {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
    assert convert_to_rub(result1) == 634531.56
