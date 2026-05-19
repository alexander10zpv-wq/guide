"""
Проверка задачи урока 12.
Запуск:  python check.py
"""

import sys
import traceback
from enum import Enum


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

    def check_enum():
        assert issubclass(task.OrderStatus, Enum), "OrderStatus должен быть Enum"
        expected = {"NEW": "new", "PAID": "paid", "SHIPPED": "shipped", "CANCELLED": "cancelled"}
        actual = {m.name: m.value for m in task.OrderStatus}
        assert actual == expected, f"ожидалось {expected}, получили {actual}"

    def check_status_label():
        assert task.status_label(task.OrderStatus.NEW) == "new"
        assert task.status_label(task.OrderStatus.PAID) == "paid"

    def check_parse_status():
        assert task.parse_status("paid") == task.OrderStatus.PAID
        assert task.parse_status("new") == task.OrderStatus.NEW
        assert task.parse_status("xxx") is None

    def check_is_finalized():
        assert task.is_finalized(task.OrderStatus.SHIPPED) is True
        assert task.is_finalized(task.OrderStatus.CANCELLED) is True
        assert task.is_finalized(task.OrderStatus.NEW) is False
        assert task.is_finalized(task.OrderStatus.PAID) is False

    def check_all_statuses():
        r = task.all_statuses()
        assert r == ["new", "paid", "shipped", "cancelled"], f"получили {r}"

    results.append(run_check("OrderStatus", check_enum))
    results.append(run_check("status_label", check_status_label))
    results.append(run_check("parse_status", check_parse_status))
    results.append(run_check("is_finalized", check_is_finalized))
    results.append(run_check("all_statuses", check_all_statuses))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
