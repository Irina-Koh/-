import pandas as pd


def reading_transactions_csv(file: str) -> list[dict]:
    """
     Загружает финансовые транзакции из указанного csv-файла.

    :param file: Путь до csv-файла с данными о транзакциях.
    :return: Список словарей с информацией о транзакциях или пустой список,
             если файл некорректен или не существует.
    """
    try:
        df_csv = pd.read_csv(file)
        transactions_csv_list = df_csv.to_dict(orient="records")
        return transactions_csv_list
    except FileNotFoundError:
        print(f"Ошибка: Файл {file} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


print(reading_transactions_csv("../transactions/transactions.csv"))


def reading_transactions_excel(file: str) -> list[dict]:
    """
     Загружает финансовые транзакции из указанного xlsx, xls-файла.

    :param file: Путь до xlsx, xls -файла с данными о транзакциях.
    :return: Список словарей с информацией о транзакциях или пустой список,
             если файл некорректен или не существует.
    """
    try:
        df_excel = pd.read_excel(file)
        transactions_excel_list = df_excel.to_dict(orient="records")
        return transactions_excel_list
    except FileNotFoundError:
        print(f"Ошибка: Файл {file} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []


print(reading_transactions_excel("../transactions/transactions_excel.xlsx"))
