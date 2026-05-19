"""
Финальная контрольная по типам данных Python.
Заполни места, помеченные //TODO.
"""

from collections import Counter, deque
from dataclasses import dataclass, field, replace
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP
from enum import Enum
from pathlib import Path


# //TODO 1: Enum OrderStatus с NEW, PAID, SHIPPED, CANCELLED
class OrderStatus(Enum):
    pass


# //TODO 2: dataclass Product с полями id: int, name: str, price: Decimal, category: str
@dataclass
class Product:
    pass


# //TODO 3: dataclass Order
# поля: id: int, items: list[Product], status: OrderStatus = OrderStatus.NEW,
# created_at: datetime = field(default_factory=datetime.now)
# Метод total(self) -> Decimal
@dataclass
class Order:
    pass

    def total(self):
        # //TODO 3
        return None


def find_product(products, product_id):
    """Вернуть Product с id == product_id, или None."""
    # //TODO 4
    return None


def unique_categories(products):
    """Множество уникальных категорий."""
    # //TODO 5
    return None


def top_categories(products, n):
    """Список из n самых частых категорий (без счётчиков)."""
    # //TODO 6
    return None


def process_orders(orders):
    """Через deque извлечь все заказы по очереди и вернуть список их id."""
    # //TODO 7
    return None


def mark_paid(order):
    """Вернуть новый Order со status=PAID. Исходный не менять."""
    # //TODO 8
    return None


def format_total(amount):
    """Округлить до 2 знаков ROUND_HALF_UP, вернуть '<amount> $'."""
    # //TODO 9
    return None


def safe_get_name(product):
    """product.name либо 'unknown' если product is None."""
    # //TODO 10
    return None


def save_order_summary(path, order):
    """Записать в path строку 'Order #<id>, status=<value>, total=<format_total>'."""
    # //TODO 11
    return None


def load_order_summary(path):
    """Прочитать файл, либо '' если файла нет."""
    # //TODO 12
    return None


def encode_summary(text):
    """Закодировать text в bytes (UTF-8)."""
    # //TODO 13
    return None


if __name__ == "__main__":
    p1 = Product(1, "Phone", Decimal("499.99"), "electronics")
    p2 = Product(2, "Book", Decimal("19.50"), "books")
    p3 = Product(3, "Laptop", Decimal("1299.00"), "electronics")
    products = [p1, p2, p3]

    order = Order(id=100, items=[p1, p2])
    print("total:", order.total())
    print("find_product(2):", find_product(products, 2))
    print("unique_categories:", unique_categories(products))
    print("top_categories:", top_categories(products, 1))
    print("process_orders:", process_orders([Order(id=1, items=[]), Order(id=2, items=[])]))
    print("mark_paid:", mark_paid(order))
    print("format_total:", format_total(Decimal("123.456")))
    print("safe_get_name(None):", safe_get_name(None))
