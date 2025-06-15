from datetime import datetime


def filter_by_state(banking_operation_state: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция, которая принимает список словарей и возращает новый список словарей по ключу state
    """
    new_banking_operation_state = []
    for operation in banking_operation_state:  # перебираем значения по ключу и добавляем в новый список
        if "state" in operation:
            if operation.get("state") == state:
                new_banking_operation_state.append(operation)
    return new_banking_operation_state


def sort_by_date(banking_operation_date: list[dict], reverse: bool = True) -> list[dict]:
    """
    Функция, которая принимает список словарей и возращает отсортированный список словарей по дате
    """
    try:
        return sorted(
            banking_operation_date,
            key=lambda operation: datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f"),
            reverse=reverse,
        )
    except KeyError:
        return "Введены некорректные данные"
