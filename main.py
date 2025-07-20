from src.utils import load_transactions
from config import file_path
from src.reading_transactions import reading_transactions_csv, reading_transactions_excel
from src.processing import filter_by_state, sort_by_date
from src.external_api import convert_to_rub
from src.process_bank_search import process_bank_search
from src.widget import mask_account_card
from datetime import datetime


# Открытие файла с выбором формата
def open_file():
    """
    Позволяет пользователю выбрать необходимый фaйл.
    :return: список транзакций
    """
    menu_items = {"1": "JSON-файл", "2": "CSV-файл", "3": "XLSX-файл"}
    while True:
        print(
            "Привет! Добро пожаловать в программу работы с банковскими транзакциями."
            "\nВыберите необходимый пункт меню:"
            "\n1. Получить информацию о транзакциях из JSON-файла"
            "\n2. Получить информацию о транзакциях из CSV-файла"
            "\n3. Получить информацию о транзакциях из XLSX-файла"
        )
        user_choice = input().strip()

        if user_choice in menu_items:
            print(f"Ваш выбор: {menu_items[user_choice]} ")
            break
        else:
            print("Такой опции нет.")

    # Загрузка файла выбранного типа
    if user_choice == "1":
        data = load_transactions(file_path)
    elif user_choice == "2":
        data = reading_transactions_csv("./transactions/transactions.csv")
    elif user_choice == "3":
        data = reading_transactions_excel("./transactions/transactions_excel.xlsx")
    return data


# Фильтрация по статусу транзакций
def filter_status(data):
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]

    while True:
        print("Введите статус для фильтрации: EXECUTED / CANCELED / PENDING")
        chosen_status = input().strip().upper()

        if chosen_status in valid_statuses:
            print(f"Транзакции будут отфильтрованы по статусу '{chosen_status}'.")
            return filter_by_state(data, state=chosen_status)
        else:
            print(f"Статус '{chosen_status}' недоступен. Выберите доступный статус.")


def sorted_date(data):
    """
    Функция для взаимодействия с пользователем и сортировки данных по дате.

    :param data: Список банковских операций (предполагается наличие поля 'date' формата YYYY-MM-DD)
    :return: Отсортированный список операций
    """
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_response_3 = input().strip().upper()

        if user_response_3 == "ДА":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                user_response_4 = input().upper().strip()

                if user_response_4 == "ВОЗРАСТАНИЮ":
                    sort_data = sort_by_date(data, reverse=False)
                    return sort_data
                elif user_response_4 == "УБЫВАНИЮ":
                    sort_data = sort_by_date(data, reverse=True)
                    return sort_data
                else:
                    print(f'Варианта ответа "{user_response_4}" в меню нет.')
        elif user_response_3 == "НЕТ":
            return data
        else:
            print(f'Варианта ответа "{user_response_3}" в меню нет.')


def currency_transaction(sort_data):
    """
    Запрашивает у пользователя вывод только рублевых транзакций.
    Если выбран да, преобразует транзакции в рубли.
    """
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_response_5 = input().upper().strip()

        if user_response_5 == "ДА":
            convert_data = convert_to_rub(sort_data)
            return convert_data
        elif user_response_5 == "НЕТ":
            return sort_data
        else:
            print(f'Варианта ответа "{user_response_5}" в меню нет.')


def filter_description(convert_data):
    """
    Позволяет пользователю выбрать фильтрацию транзакций по словам описания.
    """
    while True:
        print("Отфильтровать список транзакций по определённому слову в описании? Да/Нет")
        user_response_6 = input().upper().strip()

        if user_response_6 == "ДА":
            categories = {
                "1": "Перевод организации",
                "2": "Открытие вклада",
                "3": "Перевод со счёта на карту",
                "4": "Перевод со счёта на счёт",
                "5": "Перевод с карты на карту",
                "6": "Перевод с карты на счёт",
            }

            print("\nВыберите категорию для фильтрации:\n")
            for k, v in categories.items():
                print(f"{k}. {v}")

            while True:
                user_response_7 = input().strip().upper()
                if user_response_7 in categories.keys():
                    selected_category = categories[user_response_7]
                    data_process = process_bank_search(convert_data, search=selected_category)
                    return data_process
                else:
                    print(f"\nВарианта ответа {user_response_7} в меню нет.\nПопробуйте снова!")
        elif user_response_6 == "НЕТ":
            return convert_data
        else:
            print(f"\nВарианта ответа '{user_response_6}' в меню нет.\nПопробуйте снова!")


def main():
    try:
        file_data = open_file()
        filtered_by_status = filter_status(file_data)
        sorted_by_date = sorted_date(filtered_by_status)
        processed_currency = currency_transaction(sorted_by_date)
        final_data = filter_description(processed_currency)
        if len(final_data) == 0:
            print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(final_data)}")
        for operation in final_data:
            date_operation = operation.get("date", "")

            if date_operation:
                # Полноценный формат ISO 8601
                datetime_operation = datetime.strptime(date_operation, "%Y-%m-%dT%H:%M:%S.%f")
                formatted_date = datetime_operation.strftime("%d.%m.%Y %H:%M:%S")
            else:
                formatted_date = ""
            description_operation = operation.get("description", "")

            # Проверяем наличие полей "from" и "to"
            from_operation = mask_account_card(operation.get("from", ""))
            to_operation = mask_account_card(operation.get("to", ""))

            amount = operation.get("operationAmount", {}).get("amount", "")
            currency = operation.get("operationAmount", {}).get("currency", {}).get("name", "")

            # Выводим информацию о каждой операции

            print(f"{formatted_date} {description_operation}")
            print(f"{from_operation} -> {to_operation}")
            print(f"Сумма: {amount} {currency}")
            print()  # Добавляем пустую строку между операциями для лучшей читаемости

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
