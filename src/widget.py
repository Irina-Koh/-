from src.masks import get_mask_account, get_mask_card_number
def mask_account_card(type_and_number: str) -> str:
    '''
    функция содержит информацию о типе и номере карты или счета
    '''

    lower_type_and_number = type_and_number.lower()
    number = ''
    for char in lower_type_and_number:  # отдельно записываем номер карты или счета
        if char.isdigit():
            number = number + char

    if 'счет' in  lower_type_and_number:  # проверяем тип данных и маскируем номер счета или карты
        account_example = number
        masked_account = get_mask_account(account_example)
        new_tupe_and_number = f'Счет: {masked_account}'
    elif 'visa platinum' in lower_type_and_number:
        card_example = number
        masked_card = get_mask_card_number(card_example)
        new_tupe_and_number = f'Visa Platinun: {masked_card}'
    elif 'maestro' in lower_type_and_number:
        card_example = number
        masked_card = get_mask_card_number(card_example)
        new_tupe_and_number = f'Maestro: {masked_card}'
    return new_tupe_and_number


def get_date(date: str) -> str:
    day = date[8:10]
    month = date[5:7]
    year = date[0:4]
    new_date = f'{day}.{month}.{year}'
    return new_date




