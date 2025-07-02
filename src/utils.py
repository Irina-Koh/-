import json
from config import file_path


# Абсолютный путь к текущему рабочему каталогу#abs_path = os.getcwd()

# Использование pathlib для построения абсолютного пути


def load_transactions(file_path: str) -> dict:
    """
    Загружает финансовые транзакции из указанного JSON-файла.

    :param file_path: Путь до JSON-файла с данными о транзакциях.
    :return: Список словарей с информацией о транзакциях или пустой список,
             если файл некорректен или не существует.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Проверка типа загруженных данных
        if isinstance(data, list):
            return print(data)
        else:
            print("Ошибка: Данные в файле не являются списком.")
            return []
    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Невозможно декодировать JSON из файла {file_path}.")
        return []

load_transactions(file_path)
