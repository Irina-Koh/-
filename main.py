from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card, get_date


def main():
    card_example = "7000792289606361"
    account_example = "73654108430135874305"
    type_and_number = "visa platinum 7000792289606361"
    date = "2024-03-11T02:26:18.671407"
    masked_card = get_mask_card_number(card_example)
    masked_account = get_mask_account(account_example)
    mask_account_or_card = mask_account_card(type_and_number)
    masked_date = get_date(date)
    print("Маскированная карта:", masked_card)
    print("Маскированный счёт:", masked_account)
    print(mask_account_or_card)
    print(masked_date)


if __name__ == "__main__":
    main()
