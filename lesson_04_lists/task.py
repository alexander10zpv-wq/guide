"""
Урок 4. Списки list.
Заполни места, помеченные //TODO.
"""

# //TODO 1: создай список fruits с тремя элементами
fruits = None


def add_item(items, value):
    """Добавить value в конец items и вернуть items."""
    # //TODO 2
    return None


def remove_item(items, value):
    """Удалить первое вхождение value. Если нет — вернуть items без изменений."""
    # //TODO 3
    return None


def sum_positive(numbers):
    """Вернуть сумму положительных элементов списка."""
    # //TODO 4
    return None


def unique_sorted(items):
    """Вернуть новый отсортированный список без дублей."""
    # //TODO 5
    return None


def squares_of_evens(n):
    """Вернуть список квадратов чётных чисел в диапазоне [0, n)."""
    # //TODO 6
    return None


if __name__ == "__main__":
    print("fruits =", fruits)
    print("add_item([1, 2], 3) =", add_item([1, 2], 3))
    print("remove_item([1, 2, 3], 2) =", remove_item([1, 2, 3], 2))
    print("sum_positive([-1, 2, -3, 4]) =", sum_positive([-1, 2, -3, 4]))
    print("unique_sorted([3, 1, 2, 1, 3]) =", unique_sorted([3, 1, 2, 1, 3]))
    print("squares_of_evens(6) =", squares_of_evens(6))
