from typing import Union


def mask_account_card(account_card: str) -> str:
    # функция маскирует номер карты или счета
    if len(account_card) >= 30 or not account_card.isdigit():
        return f"{account_card[:-12]} {account_card[-12:-10]}** **** {account_card[-4:]}"
    elif len(account_card) == 20 or not account_card.isdigit():
        return f"**{account_card[-4:]}"


print(mask_account_card("Visa Gold 5999414228426353"))


def get_date(date: str) -> str:
    # функция формирует дату
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))
