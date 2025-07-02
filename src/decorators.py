import datetime


def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.datetime.now()
            start_time_string = start_time.strftime("%H:%M:%S")
            message_1 = f"function start time: {start_time_string}"
            try:
                result = func(*args, **kwargs)
                message_2 = f"Function {func.__name__} executed successfully with result: {result}"
                end_time = datetime.datetime.now()
                end_time_string = end_time.strftime("%H:%M:%S")
                message_3 = f"function end time: {end_time_string}"
                if filename is not None:
                    # Запись в файл
                    with open(filename, "a") as file:
                        file.write(message_1 + "\n" + message_2 + "\n" + message_3 + "\n")
                else:
                    # Вывод в консоль
                    print(message_1, message_2, message_3)
                return result
            except Exception as e:
                error_message = (
                    f"Error in function {func.__name__}: " f"{type(e).__name__}, args={args}, kwargs={kwargs}"
                )

                if filename is not None:
                    # Запись в файл
                    with open(filename, "a") as file:
                        file.write(error_message + "\n")
                else:
                    # Вывод в консоль
                    print(error_message)

        return wrapper

    return decorator
