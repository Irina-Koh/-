import json
from config import file_path
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename="./logs/utils.log", encoding="utf-8", mode="w")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> list:
    """
    Загружает финансовые транзакции из указанного JSON-файла.

    :param file_path: Путь до JSON-файла с данными о транзакциях.
    :return: Список словарей с информацией о транзакциях или пустой список,
             если файл некорректен или не существует.
    """
    try:
        logger.info("Открытие файла для чтения")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.info("Проверка является ли файл списком")
        # Проверка типа загруженных данных
        if isinstance(data, list):
            return data
        else:
            logger.error("Ошибка: Данные в файле не являются списком.")
            print("Ошибка: Данные в файле не являются списком.")
            return []
    except FileNotFoundError:
        logger.error(f"Файл {file_path} не найден")
        print(f"Ошибка: Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        logger.error(f"Невозможно декодировать JSON из файлф {file_path}")
        print(f"Ошибка: Невозможно декодировать JSON из файла {file_path}.")
        return []
