"""
Урок 9. NoneType.
Заполни места, помеченные //TODO.
"""


def safe_divide(a, b):
    """Вернуть a / b, или None если b == 0."""
    # //TODO 1
    return None


def first_or_none(items):
    """Вернуть первый элемент или None, если список пуст."""
    # //TODO 2
    return None


def find_index(items, value):
    """Вернуть индекс первого вхождения value, или None если нет."""
    # //TODO 3
    return None


def default_if_none(value, default):
    """Вернуть value, если оно не None, иначе default. Используй 'is None'."""
    # //TODO 4
    return None


def count_none(items):
    """Сколько элементов в items равны None."""
    # //TODO 5
    return None


if __name__ == "__main__":
    print("safe_divide(10, 2) =", safe_divide(10, 2))
    print("safe_divide(10, 0) =", safe_divide(10, 0))
    print("first_or_none([]) =", first_or_none([]))
    print("first_or_none([1, 2]) =", first_or_none([1, 2]))
    print("find_index([1, 2, 3], 2) =", find_index([1, 2, 3], 2))
    print("default_if_none(None, 'x') =", default_if_none(None, "x"))
    print("count_none([1, None, 2, None, None]) =", count_none([1, None, 2, None, None]))
