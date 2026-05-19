"""
Урок 12. Enum.
Заполни места, помеченные //TODO.
"""

from enum import Enum


# //TODO 1: создай класс OrderStatus(Enum) с 4 значениями
class OrderStatus(Enum):
    pass


def status_label(status):
    """Вернуть строковое значение OrderStatus."""
    # //TODO 2
    return None


def parse_status(text):
    """Строка -> OrderStatus, или None если значение неизвестно."""
    # //TODO 3
    return None


def is_finalized(status):
    """True, если статус SHIPPED или CANCELLED."""
    # //TODO 4
    return None


def all_statuses():
    """Список всех значений OrderStatus в порядке объявления."""
    # //TODO 5
    return None


if __name__ == "__main__":
    print("OrderStatus members:", list(OrderStatus))
    print("status_label(OrderStatus.NEW) =", status_label(OrderStatus.NEW))
    print("parse_status('paid') =", parse_status("paid"))
    print("parse_status('xxx') =", parse_status("xxx"))
    print("is_finalized(OrderStatus.SHIPPED) =", is_finalized(OrderStatus.SHIPPED))
    print("all_statuses() =", all_statuses())
