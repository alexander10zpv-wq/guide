"""
Урок 16. typing.
Заполни места, помеченные //TODO. Не забывай про аннотации типов!
"""

from typing import Literal, TypedDict


def add(a: int, b: int) -> int:
    """Сумма двух int."""
    # //TODO 1
    return None


def find_first(items, value):
    """Индекс первого вхождения value, либо None."""
    # //TODO 2: добавь аннотации: items: list[int], value: int -> int | None
    return None


def get_name(user):
    """Вернуть user['name']."""
    # //TODO 3: добавь аннотации: user: dict[str, str] -> str
    return None


def set_mode(mode):
    """Вернуть 'mode: <mode>'. mode — один из 'read', 'write', 'append'."""
    # //TODO 4: добавь аннотации: mode: Literal['read', 'write', 'append'] -> str
    return None


# //TODO 5: создай TypedDict UserDict с полями name: str, age: int
class UserDict(TypedDict):
    pass


def make_user(name, age):
    """Вернуть UserDict с полями name и age."""
    # //TODO 5: добавь аннотации: name: str, age: int -> UserDict
    return None


if __name__ == "__main__":
    print(add(1, 2))
    print(find_first([1, 2, 3], 2))
    print(get_name({"name": "Alex"}))
    print(set_mode("read"))
    print(make_user("Alex", 25))
