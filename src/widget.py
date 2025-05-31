from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """
    функция содержит информацию о типе и номере карты или счета
    """
    lower_type_and_number = type_and_number.lower()
    number = ""
    for char in lower_type_and_number:  #  отдельно записываем номер карты или счета
        if char.isdigit():
            number = number + char
            if len(number) == 20 and "счет" in lower_type_and_number:  # проверяем тип данных и маскируем номер счета или карты
                account_example = number
                masked_account = get_mask_account(account_example)
                new_tupe_and_number = f"Счет: {masked_account}"
                return new_tupe_and_number
            elif (len(number) == 16 and "visa platinum" in lower_type_and_number):
                card_example = number
                masked_card = get_mask_card_number(card_example)
                new_tupe_and_number = f"Visa Platinum: {masked_card}"
                return new_tupe_and_number
            elif len(number) == 16 and "maestro" in lower_type_and_number:
                card_example = number
                masked_card = get_mask_card_number(card_example)
                new_tupe_and_number = f"Maestro: {masked_card}"
                return new_tupe_and_number
            elif len(number) == 16 and "mastercard" in lower_type_and_number:
                card_example = number
                masked_card = get_mask_card_number(card_example)
                new_tupe_and_number = f"MasterCard: {masked_card}"
                return new_tupe_and_number
            elif len(number) == 16 and "visa classic" in lower_type_and_number:
                card_example = number
                masked_card = get_mask_card_number(card_example)
                new_tupe_and_number = f"Visa Classic: {masked_card}"
                return new_tupe_and_number
            elif len(number) == 16 and "visa gold" in lower_type_and_number:
                card_example = number
                masked_card = get_mask_card_number(card_example)
                new_tupe_and_number = f"Visa Gold: {masked_card}"
                return new_tupe_and_number
    else:
        return "Введены некорректные данные"





def get_date(date: str) -> str:
    """
    Функция для форматирования даты
    """
    if len(date) == 26 and str(date[4]) == '-' and str(date[7]) == '-' and str(date[10]) == 'T' and str(date[13]) == ':' and str(date[16]) == ':' and str(date[19]) == '.':
        day = date[8:10]  #"2024-03-11T02:26:18.671407" #,5:7,0:4,11:13,14:16,17:19,20:-1
        month = date[5:7]
        year = date[0:4]
        if day.isdigit() and day != '00' and int(day) < 32  and month.isdigit() and month != '00' and int(month) < 13  and year.isdigit() and year != '0000':
            if int(year) % 100 == 0 and int(year) % 400 != 0 and month == '02' and int(day) < 29:
                return f"{day}.{month}.{year}"
            elif int(year) % 100 == 0 and int(year) % 400 == 0 and month == '02' and int(day) < 30:
                return f"{day}.{month}.{year}"
            elif int(year) % 4 == 0 and month == '02' and int(day) < 30:
                return f"{day}.{month}.{year}"
            elif month == "01" or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12' and day < 32:
                return f"{day}.{month}.{year}"
            elif month == "04" or month == '06' or month == '09' or month == '11'  and day < 31:
                return f"{day}.{month}.{year}"
            else:
                return 'Такой даты не существует'
        else:
            return 'Введены некорректные данные'
    else:
        return 'Введены некорректные данные'