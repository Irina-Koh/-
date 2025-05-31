from src.masks import get_mask_account, get_mask_card_number


def test_masks():
    assert get_mask_card_number("1596837868705199") == "15968 37** **** 199"
    assert get_mask_card_number("896548452145") == "Неккоректные данные. Номер карты состоит из 16 цифр"
    assert get_mask_card_number("") == "Неккоректные данные. Номер карты состоит из 16 цифр"
    assert get_mask_card_number("fgh45895EEE") == "Неккоректные данные. Номер карты состоит из 16 цифр"


def test_account():
    assert get_mask_account("64686473678894779589") == "**9589"
    assert get_mask_account("6468647394779589") == "Неккоректные данные. Номер счета состоит из 20 цифр"
    assert get_mask_account("") == "Неккоректные данные. Номер счета состоит из 20 цифр"
    assert get_mask_account("64686473TTT67j89") == "Неккоректные данные. Номер счета состоит из 20 цифр"
