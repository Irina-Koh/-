from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date


def main() -> None:
    card_example = '5999414228426353'
    account_example = '73654108430135874305'
    type_and_number = "счет 73654108430135874305"
    date = "2031-02-29T02:26:18.671400"
    banking_operation = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    state = "EXECUTED"
    reverse = True
    banking_operation_date = sort_by_date(banking_operation, reverse)
    banking_operation_new = filter_by_state(banking_operation, state)
    masked_card = get_mask_card_number(card_example)
    masked_account = get_mask_account(account_example)
    mask_account_or_card = mask_account_card(type_and_number)
    masked_date = get_date(date)

    print(banking_operation_date)
    print(banking_operation_new)
    print("Маскированная карта:", masked_card)
    print("Маскированный счёт:", masked_account)
    print(mask_account_or_card)
    print(masked_date)


if __name__ == "__main__":
    main()

