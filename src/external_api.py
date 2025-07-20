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
