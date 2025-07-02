import random

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
    {},
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency"
            "": {
                "name": "руб.",
            },
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list[dict], currency_code="USD"):
    """Фильтрует транзакции по заданному коду валюты и возвращает итератор."""
    try:
        for transaction in transactions:
            if transaction["operationAmount"]["currency"]["code"] == currency_code:
                yield transaction
    except KeyError:
        return "Введены некорректные данные"


# Фильтрация транзакций с валютой USD
usd_transactions = filter_by_currency(transactions, currency_code="USD")
print(next(usd_transactions))


def transaction_descriptions(transactions):
    """
    Функция,которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди
    """
    try:
        for transaction in transactions:
            yield transaction["description"]
    except KeyError:
        return "Введены некорректные данные"


descriptions = transaction_descriptions(transactions)


def card_number_generator(start, stop):
    """
    Генерирует случайный номер банковской карты в указанном диапазоне.

    :param start: минимальное значение диапазона (включительно)
    :param stop: максимальное значение диапазона (включительно)
    :return: строка формата 'XXXX XXXX XXXX XXXX'
    """
    # Генерация случайного числа в пределах указанного диапазона

    if start > 0 and stop < 10000000000000000 and start <= stop:
        number = str(random.randint(start, stop))
        # Добавляем ведущие нули, если число меньше максимального количества цифр
        while len(number) < 16:
            number = "0" + number
        # Форматируем строку согласно банковскому стандарту (группы по четыре цифры)
        formatted_number = " ".join([number[i : i + 4] for i in range(0, len(number), 4)])
        yield formatted_number
    else:
        return "Введены некорректные данные"


card_number = card_number_generator(start=1, stop=5)
