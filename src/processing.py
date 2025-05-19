from datetime import datetime


def filter_by_state(banking_operation: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция, которая принимает список словарей и возращает новый список словарей по ключу state
    """
    new_banking_operation = []
    for operation in banking_operation:  # перебираем значения по ключу и добавляем в новый список
        if "state" in operation:
            if operation.get("state") == state:
                new_banking_operation.append(operation)
    return new_banking_operation


def sort_by_date(banking_operation: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция, которая принимает список словарей и возращает отсортированный список словарей по дате
    """
    return sorted(
        banking_operation,
        key=lambda operation: datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse,
    )

