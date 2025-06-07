from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def main() -> None:
    card_example = "5999414228426353"
    account_example = "73654108430135874305"
    type_and_number = "Visa Classic 7365410843013587"
    date = "1900-02-29T02:26:18.671400"
    banking_operation_state = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
        {},
        {"id": 615064591, "date": "2018-09-12T08:21:33.419441"},
    ]
    banking_operation_date = [{}]
    name = "USD"
    transactions =(
        [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
    )
    state = "EXECUTED"
    reverse = True


    banking_operation_date = sort_by_date(banking_operation_date, reverse)
    banking_operation_new = filter_by_state(banking_operation_state, state)
    masked_card = get_mask_card_number(card_example)
    masked_account = get_mask_account(account_example)
    mask_account_or_card = mask_account_card(type_and_number)
    masked_date = get_date(date)
    transactions_usd = filter_by_currency(transactions,currency_code="USD")
    descriptions_ = transaction_descriptions(transactions)
    card_number_ = card_number_generator(start=1, stop=9999999999999999)
    print(banking_operation_date)
    print(banking_operation_new)
    print("Маскированная карта:", masked_card)
    print("Маскированный счёт:", masked_account)
    print(mask_account_or_card)
    print(masked_date)
    print(next(transactions_usd))
    print(next(transactions_usd))
    print(next(transactions_usd))
    print(next(descriptions_))
    print(next(descriptions_))
    print(next(descriptions_))
    print(next(descriptions_))
    print(next(descriptions_))
    print(next(card_number_))

if __name__ == "__main__":
    main()
