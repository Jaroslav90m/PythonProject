def filter_by_state(data, state="EXECUTED"):
    result = []  # Создаем пустой список для хранения результатов
    for item in data:
        if item["state"] == state:
            result.append(item)
    return result


# Пример входных данных для проверки функции
data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Вызов функции с использованием статуса по умолчанию 'EXECUTED'
executed_transactions = filter_by_state(data)
print(executed_transactions)

# Вызов функции с передачей статуса 'CANCELED'
canceled_transactions = filter_by_state(data, "CANCELED")
print(canceled_transactions)
