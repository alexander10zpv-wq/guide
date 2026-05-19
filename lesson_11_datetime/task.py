"""
Урок 11. datetime, date, timedelta.
Заполни места, помеченные //TODO.
"""

from datetime import date, datetime, timedelta


def days_between(date1, date2):
    """Число дней между двумя датами (всегда >= 0)."""
    # //TODO 1
    return None


def add_days(start_date, n):
    """Вернуть date через n дней от start_date."""
    # //TODO 2
    return None


def format_date(d):
    """Вернуть строку 'DD.MM.YYYY'."""
    # //TODO 3
    return None


def parse_date(text):
    """Строка 'YYYY-MM-DD' -> date."""
    # //TODO 4
    return None


def is_weekend(d):
    """True, если d — суббота или воскресенье."""
    # //TODO 5
    return None


if __name__ == "__main__":
    print("days_between(date(2026,5,1), date(2026,5,19)) =",
          days_between(date(2026, 5, 1), date(2026, 5, 19)))
    print("add_days(date(2026,5,1), 10) =", add_days(date(2026, 5, 1), 10))
    print("format_date(date(2026,5,19)) =", format_date(date(2026, 5, 19)))
    print("parse_date('2026-05-19') =", parse_date("2026-05-19"))
    print("is_weekend(date(2026,5,17)) =", is_weekend(date(2026, 5, 17)))  # вс
