"""
Проверка задачи урока 11.
Запуск:  python check.py
"""

import sys
import traceback
from datetime import date


def run_check(name, func):
    try:
        func()
        print(f"[OK]  {name}")
        return True
    except AssertionError as e:
        print(f"[FAIL] {name}: {e}")
    except Exception as e:
        print(f"[ERROR] {name}: {type(e).__name__}: {e}")
        traceback.print_exc()
    return False


def main():
    try:
        import task
    except Exception as e:
        print(f"Не удалось импортировать task.py: {type(e).__name__}: {e}")
        sys.exit(1)

    results = []

    def check_days_between():
        assert task.days_between(date(2026, 5, 1), date(2026, 5, 19)) == 18
        assert task.days_between(date(2026, 5, 19), date(2026, 5, 1)) == 18
        assert task.days_between(date(2026, 5, 1), date(2026, 5, 1)) == 0

    def check_add_days():
        assert task.add_days(date(2026, 5, 1), 10) == date(2026, 5, 11)
        assert task.add_days(date(2026, 5, 1), 0) == date(2026, 5, 1)
        assert task.add_days(date(2026, 12, 31), 1) == date(2027, 1, 1)

    def check_format_date():
        assert task.format_date(date(2026, 5, 19)) == "19.05.2026"
        assert task.format_date(date(2000, 1, 1)) == "01.01.2000"

    def check_parse_date():
        assert task.parse_date("2026-05-19") == date(2026, 5, 19)
        assert task.parse_date("2000-01-01") == date(2000, 1, 1)

    def check_is_weekend():
        assert task.is_weekend(date(2026, 5, 17)) is True   # воскресенье
        assert task.is_weekend(date(2026, 5, 16)) is True   # суббота
        assert task.is_weekend(date(2026, 5, 18)) is False  # понедельник

    results.append(run_check("days_between", check_days_between))
    results.append(run_check("add_days", check_add_days))
    results.append(run_check("format_date", check_format_date))
    results.append(run_check("parse_date", check_parse_date))
    results.append(run_check("is_weekend", check_is_weekend))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
