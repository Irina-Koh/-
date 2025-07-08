import requests
import os
from dotenv import load_dotenv
from config import current_dir

load_dotenv(current_dir / ".env")
API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"
print(API_KEY)


def convert_to_rub(transaction: dict) -> float:
    """Конвертирует сумму транзакции из исходной валюты в рубли по текущему курсу."""
    try:
        # Проверка наличия API ключа
        if not API_KEY:
            raise ValueError("API key not configured")

        # Извлечение данных
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"].upper()

        if currency == "RUB":
            return amount

        if currency not in ("USD", "EUR"):
            raise ValueError(f"Неподдерживаемая валюта: {currency}")

        # Запрос к API
        response = requests.get(
            BASE_URL, params={"to": "RUB", "from": currency, "amount": amount}, headers={"apikey": API_KEY}, timeout=10
        )
        response.raise_for_status()

        data = response.json()
        # Проверка успешности ответа
        if not data.get("success", True):
            error_info = data.get("error", {}).get("info", "Unknown API error")
            raise ValueError(f"API error: {error_info}")
        return round(data["result"], 2)

    except KeyError as e:
        raise ValueError(f"Missing required field in transaction: {e}")
    except requests.exceptions.RequestException as e:
        raise ValueError(f"API connection error: {str(e)}")


if __name__ == "__main__":
    transaction = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]
    for t in transaction:
        result = convert_to_rub(t)
        print(f"Транзакция: {t}, Сумма в рублях: {result}")
