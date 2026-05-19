"""
Урок 17. Выбор подходящего типа.
Заполни строковые ответы в местах //TODO.
Допустимые ответы (как строки):
  "int", "float", "Decimal", "str", "bool",
  "list", "tuple", "set", "dict",
  "dataclass", "Enum", "datetime", "deque", "Counter",
  "bytes", "None", "TypedDict"
"""

# //TODO 1: Цена товара — без ошибок округления
answer_money = ""

# //TODO 2: Уникальный целочисленный ID пользователя
answer_user_id = ""

# //TODO 3: Фиксированная пара координат (x, y)
answer_coordinates = ""

# //TODO 4: Набор уникальных тегов поста
answer_unique_tags = ""

# //TODO 5: Фиксированный список статусов заказа (new/paid/shipped/cancelled)
answer_order_status = ""

# //TODO 6: Структурированный объект пользователя в backend-логике
answer_business_user = ""

# //TODO 7: Подсчёт количества повторений каждого слова в тексте
answer_word_frequency = ""

# //TODO 8: Очередь задач FIFO
answer_task_queue = ""

# //TODO 9: Момент времени события
answer_event_timestamp = ""

# //TODO 10: "Значение отсутствует / не найдено"
answer_missing_value = ""


if __name__ == "__main__":
    for name, value in vars().copy().items():
        if name.startswith("answer_"):
            print(f"{name} = {value!r}")
