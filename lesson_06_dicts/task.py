"""
Урок 6. Словари dict.
Заполни места, помеченные //TODO.
"""

# //TODO 1: создай словарь user
user = None


def get_field(data, key):
    """Безопасно вернуть data[key] или None."""
    # //TODO 2
    return None


def set_field(data, key, value):
    """Установить data[key] = value и вернуть data."""
    # //TODO 3
    return None


def merge_dicts(a, b):
    """Вернуть новый словарь, объединяющий a и b. Значения из b побеждают."""
    # //TODO 4
    return None


def count_chars(text):
    """Вернуть словарь {символ: количество}."""
    # //TODO 5
    return None


def invert_dict(data):
    """Поменять местами ключи и значения."""
    # //TODO 6
    return None


if __name__ == "__main__":
    print("user =", user)
    print("get_field(user, 'name') =", get_field(user, "name"))
    print("merge_dicts({'a': 1}, {'a': 2, 'b': 3}) =",
          merge_dicts({"a": 1}, {"a": 2, "b": 3}))
    print("count_chars('hello') =", count_chars("hello"))
    print("invert_dict({'a': 1, 'b': 2}) =", invert_dict({"a": 1, "b": 2}))
