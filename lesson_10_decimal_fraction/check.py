"""
Проверка задачи урока 10.
Запуск:  python check.py
"""

import sys
import traceback
from decimal import Decimal
from fractions import Fraction


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

    def check_add_money():
        r = task.add_money("1.10", "2.20")
        assert isinstance(r, Decimal), f"должно быть Decimal, а {type(r).__name__}"
        assert r == Decimal("3.30"), f"ожидалось 3.30, получили {r}"

    def check_apply_tax():
        r = task.apply_tax("100", "0.20")
        assert isinstance(r, Decimal)
        assert r == Decimal("120.00"), f"ожидалось 120.00, получили {r}"
        r2 = task.apply_tax("19.99", "0.20")
        assert r2 == Decimal("23.99"), f"ожидалось 23.99, получили {r2}"

    def check_add_fractions():
        r = task.add_fractions(1, 3, 1, 6)
        assert isinstance(r, Fraction)
        assert r == Fraction(1, 2), f"ожидалось 1/2, получили {r}"

    def check_is_exact_third():
        assert task.is_exact_third(Fraction(1, 3)) is True
        assert task.is_exact_third(Fraction(2, 6)) is True   # сокращается до 1/3
        assert task.is_exact_third(Fraction(1, 2)) is False

    def check_cents_total():
        r = task.cents_total(["1.99", "2.50"])
        assert isinstance(r, Decimal)
        assert r == Decimal("4.49"), f"ожидалось 4.49, получили {r}"
        assert task.cents_total([]) == Decimal("0")

    results.append(run_check("add_money", check_add_money))
    results.append(run_check("apply_tax", check_apply_tax))
    results.append(run_check("add_fractions", check_add_fractions))
    results.append(run_check("is_exact_third", check_is_exact_third))
    results.append(run_check("cents_total", check_cents_total))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
