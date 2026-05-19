"""
Урок 10. Decimal и Fraction.
Заполни места, помеченные //TODO.
"""

from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction


def add_money(a, b):
    """Принимает строки '19.99'. Возвращает Decimal-сумму."""
    # //TODO 1
    return None


def apply_tax(price, tax_rate):
    """price + price*tax_rate, округлено до 2 знаков ROUND_HALF_UP."""
    # //TODO 2
    return None


def add_fractions(a_num, a_den, b_num, b_den):
    """Сумма двух дробей как Fraction."""
    # //TODO 3
    return None


def is_exact_third(x):
    """True, если Fraction x равен ровно 1/3."""
    # //TODO 4
    return None


def cents_total(prices):
    """Сумма цен (строк) как Decimal."""
    # //TODO 5
    return None


if __name__ == "__main__":
    print("add_money('1.10', '2.20') =", add_money("1.10", "2.20"))
    print("apply_tax('100', '0.20') =", apply_tax("100", "0.20"))
    print("add_fractions(1, 3, 1, 6) =", add_fractions(1, 3, 1, 6))
    print("is_exact_third(Fraction(1, 3)) =", is_exact_third(Fraction(1, 3)))
    print("cents_total(['1.99', '2.50']) =", cents_total(["1.99", "2.50"]))
