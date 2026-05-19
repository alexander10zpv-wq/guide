"""
Урок 14. collections.
Заполни места, помеченные //TODO.
"""

from collections import deque, Counter, defaultdict, namedtuple


def process_queue(tasks):
    """Положить задачи в deque и извлекать по очереди слева. Вернуть список."""
    # //TODO 1
    return None


def top_words(words, n):
    """Вернуть список из n самых частых слов."""
    # //TODO 2
    return None


def group_by_first_letter(words):
    """Сгруппировать слова по первой букве: {буква: [слова]}."""
    # //TODO 3
    return None


# //TODO 4: создай namedtuple Point с полями x, y
Point = None


def make_point(x, y):
    # //TODO 4: вернуть Point(x, y)
    return None


def count_letters(text):
    """Вернуть dict {буква: количество}."""
    # //TODO 5
    return None


if __name__ == "__main__":
    print("process_queue(['a','b','c']) =", process_queue(["a", "b", "c"]))
    print("top_words(['a','b','a','c','a','b'], 2) =",
          top_words(["a", "b", "a", "c", "a", "b"], 2))
    print("group_by_first_letter(['apple','ant','bear']) =",
          group_by_first_letter(["apple", "ant", "bear"]))
    print("make_point(1, 2) =", make_point(1, 2))
    print("count_letters('hello') =", count_letters("hello"))
