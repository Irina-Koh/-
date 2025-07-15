import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename="../logs/masks.log", encoding="utf-8", mode="w")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    принимает на вход номер карты в виде строки и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    logger.info("Проверяет длину строки номера карты и наличие только цифр")
    if len(card_number) != 16 or card_number.isdigit() == False:
        logger.error("Неверный номер карты")
        return "Неккоректные данные. Номер карты состоит из 16 цифр"
    else:
        logger.info("Создает маску номера")
        number_1 = card_number[:5]  # первые четыре цифры
        number_2 = card_number[5:7]  # пятая и шестая цифра
        number_5 = card_number[13:]  # с тринадцатой по шестнадцатые цифры
        new_card_number_str = f"{number_1} {number_2}** **** {number_5}"  # соединяем в строку
        return new_card_number_str


def get_mask_account(account_number: str) -> str:
    """
    принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX
    """
    logger.info("Проверяет длину строки номера счета и наличие только цифр")
    if len(account_number) != 20 or account_number.isdigit() == False:
        logger.error("Неверный номер счета")
        return "Неккоректные данные. Номер счета состоит из 20 цифр"
    else:
        logger.info("Создает маску счета")
        number_1 = account_number[-4:]
        new_get_mask_account = f"**{number_1}"
        return new_get_mask_account


get_mask_card_number("555555555555555")
get_mask_account("99999999999999999999")
