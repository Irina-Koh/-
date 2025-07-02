from datetime import datetime
from src.decorators import log

def test_log():
    @log("my_log.txt")
    def summa(x, y):
        return x + y

    result = summa(5, 10)
    assert result == 15


def test_log(capsys):
    @log()
    def summa(x, y):
        return x + y

    result = summa(
        5,
    )
    assert result == None


def test_log(capsys):
    @log("my_log.txt")
    def summa(x, y):
        return x + y

    summa(5, 8)
    start_time_string = "12:34:56"
    end_time_string = "12:35:01"
    start_time = datetime.strptime(start_time_string, "%H:%M:%S")
    end_time = datetime.strptime(end_time_string, "%H:%M:%S")
    assert start_time < end_time, "Время окончания должно быть позже времени начала"
