from unittest import TestCase, main
from unittest.mock import patch
import pandas as pd
from src.reading_transactions import reading_transactions_csv, reading_transactions_excel


class TestReadingTransactionsCSV(TestCase):

    def test_read_valid_csv(self):
        # Подготавливаем mock DataFrame для возврата из read_csv
        mock_df = pd.DataFrame({"transaction_id": [1, 2], "amount": [100, 200]})

        with patch("pandas.read_csv", return_value=mock_df):
            result = reading_transactions_csv("test_file.csv")
            self.assertEqual(result, [{"amount": 100, "transaction_id": 1}, {"amount": 200, "transaction_id": 2}])

    @patch("pandas.read_csv")
    def test_read_nonexistent_csv(self, mock_read_csv):
        # Моделируем ошибку отсутствия файла
        mock_read_csv.side_effect = FileNotFoundError
        result = reading_transactions_csv("nonexistent_file.csv")
        self.assertEqual(result, [])

    @patch("pandas.read_csv")
    def test_read_with_exception(self, mock_read_csv):
        # Моделируем общую ошибку
        mock_read_csv.side_effect = Exception("Some error occurred")
        result = reading_transactions_csv("invalid_file.csv")
        self.assertEqual(result, [])


class TestReadingTransactionsExcel(TestCase):

    def test_read_valid_excel(self):
        # Подготавливаем mock DataFrame для возврата из read_excel
        mock_df = pd.DataFrame({"transaction_id": [1, 2], "amount": [100, 200]})

        with patch("pandas.read_excel", return_value=mock_df):
            result = reading_transactions_excel("test_file.xlsx")
            self.assertEqual(result, [{"amount": 100, "transaction_id": 1}, {"amount": 200, "transaction_id": 2}])

    @patch("pandas.read_excel")
    def test_read_nonexistent_excel(self, mock_read_excel):
        # Моделируем ошибку отсутствия файла
        mock_read_excel.side_effect = FileNotFoundError
        result = reading_transactions_excel("nonexistent_file.xlsx")
        self.assertEqual(result, [])

    @patch("pandas.read_excel")
    def test_read_with_exception(self, mock_read_excel):
        # Моделируем общую ошибку
        mock_read_excel.side_effect = Exception("Some error occurred")
        result = reading_transactions_excel("invalid_file.xlsx")
        self.assertEqual(result, [])


if __name__ == "__main__":
    main()
