"""
Урок 7. Множества set и frozenset.
Заполни места, помеченные //TODO.
"""


def unique(items):
    """Вернуть множество уникальных элементов из items."""
    # //TODO 1
    return None


def common(a, b):
    """Вернуть множество общих элементов a и b (пересечение)."""
    # //TODO 2
    return None


def union_all(lists):
    """Объединить элементы из списка списков в одно множество."""
    # //TODO 3
    return None


def only_in_first(a, b):
    """Вернуть элементы, которые есть в a, но не в b."""
    # //TODO 4
    return None


def has_duplicates(items):
    """Вернуть True, если в items есть дубликаты."""
    # //TODO 5
    return None


if __name__ == "__main__":
    print("unique([1,2,2,3]) =", unique([1, 2, 2, 3]))
    print("common([1,2,3], [2,3,4]) =", common([1, 2, 3], [2, 3, 4]))
    print("union_all([[1,2],[2,3]]) =", union_all([[1, 2], [2, 3]]))
    print("only_in_first([1,2,3], [2,3,4]) =", only_in_first([1, 2, 3], [2, 3, 4]))
    print("has_duplicates([1,2,3]) =", has_duplicates([1, 2, 3]))
