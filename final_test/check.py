"""
Проверка финальной контрольной.
Запуск:  python check.py
"""

import sys
import tempfile
import traceback
from dataclasses import is_dataclass, fields, FrozenInstanceError
from datetime import datetime
from decimal import Decimal
from enum import Enum
from pathlib import Path


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

    # ---------- 1. OrderStatus ----------
    def check_status():
        assert issubclass(task.OrderStatus, Enum), "OrderStatus должен быть Enum"
        expected = {"NEW": "new", "PAID": "paid", "SHIPPED": "shipped", "CANCELLED": "cancelled"}
        actual = {m.name: m.value for m in task.OrderStatus}
        assert actual == expected, f"ожидалось {expected}, получили {actual}"

    # ---------- 2. Product ----------
    def check_product():
        assert is_dataclass(task.Product), "Product должен быть dataclass"
        names = {f.name for f in fields(task.Product)}
        assert names == {"id", "name", "price", "category"}, \
            f"ожидались поля id,name,price,category; получили {names}"
        p = task.Product(1, "X", Decimal("9.99"), "cat")
        assert p.id == 1 and p.name == "X" and p.price == Decimal("9.99") and p.category == "cat"

    # ---------- 3. Order ----------
    def check_order():
        assert is_dataclass(task.Order), "Order должен быть dataclass"
        names = {f.name for f in fields(task.Order)}
        assert names == {"id", "items", "status", "created_at"}, \
            f"ожидались поля id,items,status,created_at; получили {names}"
        o = task.Order(id=1, items=[])
        assert o.status == task.OrderStatus.NEW, "status по умолчанию должен быть NEW"
        assert isinstance(o.created_at, datetime), "created_at должен быть datetime"

        p1 = task.Product(1, "A", Decimal("10.00"), "c")
        p2 = task.Product(2, "B", Decimal("2.50"), "c")
        o2 = task.Order(id=2, items=[p1, p2])
        assert o2.total() == Decimal("12.50"), f"total ожидалось 12.50, получили {o2.total()}"
        assert task.Order(id=3, items=[]).total() == Decimal("0")

    # ---------- 4. find_product ----------
    def check_find_product():
        p1 = task.Product(1, "A", Decimal("1"), "c")
        p2 = task.Product(2, "B", Decimal("2"), "c")
        assert task.find_product([p1, p2], 2) is p2
        assert task.find_product([p1, p2], 999) is None
        assert task.find_product([], 1) is None

    # ---------- 5. unique_categories ----------
    def check_unique_categories():
        p1 = task.Product(1, "A", Decimal("1"), "books")
        p2 = task.Product(2, "B", Decimal("2"), "books")
        p3 = task.Product(3, "C", Decimal("3"), "electronics")
        r = task.unique_categories([p1, p2, p3])
        assert isinstance(r, set), f"должно быть set, а {type(r).__name__}"
        assert r == {"books", "electronics"}, f"получили {r}"
        assert task.unique_categories([]) == set()

    # ---------- 6. top_categories ----------
    def check_top_categories():
        p1 = task.Product(1, "A", Decimal("1"), "books")
        p2 = task.Product(2, "B", Decimal("2"), "books")
        p3 = task.Product(3, "C", Decimal("3"), "electronics")
        p4 = task.Product(4, "D", Decimal("4"), "books")
        r = task.top_categories([p1, p2, p3, p4], 1)
        assert r == ["books"], f"получили {r}"
        r2 = task.top_categories([p1, p2, p3, p4], 2)
        assert r2[0] == "books" and set(r2) == {"books", "electronics"}, f"получили {r2}"

    # ---------- 7. process_orders ----------
    def check_process_orders():
        orders = [task.Order(id=1, items=[]),
                  task.Order(id=2, items=[]),
                  task.Order(id=3, items=[])]
        assert task.process_orders(orders) == [1, 2, 3]
        assert task.process_orders([]) == []

    # ---------- 8. mark_paid ----------
    def check_mark_paid():
        o = task.Order(id=10, items=[])
        new_o = task.mark_paid(o)
        assert new_o.status == task.OrderStatus.PAID, "новый должен быть PAID"
        assert o.status == task.OrderStatus.NEW, "исходный не должен меняться"
        assert new_o is not o
        assert new_o.id == 10

    # ---------- 9. format_total ----------
    def check_format_total():
        assert task.format_total(Decimal("123.456")) == "123.46 $"
        assert task.format_total(Decimal("0")) == "0.00 $"
        assert task.format_total(Decimal("19.99")) == "19.99 $"
        assert task.format_total(Decimal("2.5")) == "2.50 $"

    # ---------- 10. safe_get_name ----------
    def check_safe_get_name():
        p = task.Product(1, "Phone", Decimal("1"), "c")
        assert task.safe_get_name(p) == "Phone"
        assert task.safe_get_name(None) == "unknown"

    # ---------- 11. save / load / encode ----------
    def check_io():
        p = task.Product(1, "A", Decimal("10.00"), "c")
        order = task.Order(id=42, items=[p])
        # переведём в PAID
        order_paid = task.mark_paid(order)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "summary.txt"
            task.save_order_summary(path, order_paid)
            assert path.exists(), "файл должен быть создан"
            text = task.load_order_summary(path)
            assert "Order #42" in text, f"ожидали 'Order #42' в {text!r}"
            assert "paid" in text, f"ожидали 'paid' в {text!r}"
            assert "10.00 $" in text, f"ожидали '10.00 $' в {text!r}"
            # пропавший файл
            missing = Path(tmp) / "nope.txt"
            assert task.load_order_summary(missing) == ""
            # encode
            encoded = task.encode_summary("Привет")
            assert isinstance(encoded, bytes), f"должно быть bytes, а {type(encoded).__name__}"
            assert encoded == "Привет".encode("utf-8")

    results.append(run_check("1. OrderStatus", check_status))
    results.append(run_check("2. Product", check_product))
    results.append(run_check("3. Order + total", check_order))
    results.append(run_check("4. find_product", check_find_product))
    results.append(run_check("5. unique_categories", check_unique_categories))
    results.append(run_check("6. top_categories", check_top_categories))
    results.append(run_check("7. process_orders", check_process_orders))
    results.append(run_check("8. mark_paid", check_mark_paid))
    results.append(run_check("9. format_total", check_format_total))
    results.append(run_check("10. safe_get_name", check_safe_get_name))
    results.append(run_check("11. save/load/encode", check_io))

    print()
    if all(results):
        print("=" * 50)
        print("КОНТРОЛЬНАЯ ПРОЙДЕНА! Курс завершён.")
        print("=" * 50)
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок. Поправь ошибки выше.")
        sys.exit(1)


if __name__ == "__main__":
    main()
