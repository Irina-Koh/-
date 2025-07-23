import re
from collections import defaultdict
from collections import Counter


categories = [
    "Перевод организации",
    "Открытие вклада",
    "Перевод со счета на карту",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
    "Перевод с карты на счет",
]


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    :param data: список словарей с данными о банковских операциях
    :param search: строкa поиска
    :return:  список словарей, у которых в описании есть данная строка
    """
    try:
        new_data = []
        for operation in data:
            if "description" in operation:
                descriptions = operation.get("description")
                result = re.search(search, descriptions, flags=re.IGNORECASE)
                if result != None:
                    new_data.append(operation)
        return new_data
    except TypeError:
        print("Операция или функция применяется к объекту несоответствующего типа.")
        return []


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """

    :param data: список словарей с данными о банковских операциях
    :param categories: список категорий операций
    :return: словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    bank_operations_category = defaultdict(int)
    for i in range(len(categories)):
        bank_operations_category[categories[i]] = 0
    new_data = []
    for operation in data:
        if "description" in operation:
            description = operation.get("description")
            new_data.append(description)
    number_banking_operation = Counter(new_data)
    bank_operations_category.update(number_banking_operation)
    return bank_operations_category
