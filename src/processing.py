
def filter_by_state(banking_operation: list[dict], state: str='EXECUTED') -> list[dict]:
    '''
    Функция, которая принимает список словарей и возращает новый список словарей по ключу state
    '''
    new_banking_operation = []
    for operation in banking_operation:  #  перебираем значения по ключу и добавляем в новый список
        if 'state' in operation:
            if operation.get('state') == state:
                new_banking_operation.append(operation)
    return new_banking_operation

