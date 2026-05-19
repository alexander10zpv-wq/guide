"""
Проверка задачи урока 1.
Запуск:  python check.py
"""

import sys
import traceback


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

    def check_age():
        assert isinstance(task.age, int) and not isinstance(task.age, bool), \
            f"age должен быть int, а получил {type(task.age).__name__}"
        assert task.age == 25, f"age должен быть 25, а равен {task.age}"

    def check_price():
        assert isinstance(task.price, float), \
            f"price должен быть float, а получил {type(task.price).__name__}"
        assert task.price == 19.99, f"price должен быть 19.99, а равен {task.price}"

    def check_complex():
        assert isinstance(task.z, complex), \
            f"z должен быть complex, а получил {type(task.z).__name__}"
        assert task.z == complex(3, 4), f"z должен быть 3+4j, а равен {task.z}"

    def check_rectangle_area():
        assert task.rectangle_area(3, 4) == 12, "rectangle_area(3, 4) должно быть 12"
        assert task.rectangle_area(2.5, 4) == 10.0, "rectangle_area(2.5, 4) должно быть 10.0"
        assert task.rectangle_area(0, 5) == 0, "rectangle_area(0, 5) должно быть 0"

    def check_cents_to_dollars():
        assert task.cents_to_dollars(1234) == "12.34", \
            f'cents_to_dollars(1234) должно быть "12.34", а получили {task.cents_to_dollars(1234)!r}'
        assert task.cents_to_dollars(100) == "1.00", \
            f'cents_to_dollars(100) должно быть "1.00"'
        assert task.cents_to_dollars(5) == "0.05", \
            f'cents_to_dollars(5) должно быть "0.05" (важны ведущие нули!)'
        assert task.cents_to_dollars(0) == "0.00", "cents_to_dollars(0) должно быть '0.00'"

    results.append(run_check("age", check_age))
    results.append(run_check("price", check_price))
    results.append(run_check("z (complex)", check_complex))
    results.append(run_check("rectangle_area", check_rectangle_area))
    results.append(run_check("cents_to_dollars", check_cents_to_dollars))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок. Поправь ошибки выше.")
        sys.exit(1)


if __name__ == "__main__":
    main()
