"""
Проверка задачи урока 9.
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

    def check_safe_divide():
        assert task.safe_divide(10, 2) == 5
        assert task.safe_divide(10, 0) is None
        assert task.safe_divide(0, 5) == 0

    def check_first_or_none():
        assert task.first_or_none([]) is None
        assert task.first_or_none([1, 2, 3]) == 1
        assert task.first_or_none(["a"]) == "a"

    def check_find_index():
        assert task.find_index([1, 2, 3], 2) == 1
        assert task.find_index([1, 2, 3], 999) is None
        assert task.find_index([], 1) is None

    def check_default_if_none():
        assert task.default_if_none(None, "x") == "x"
        assert task.default_if_none(0, "x") == 0     # 0 это не None!
        assert task.default_if_none("", "x") == ""   # "" это не None!
        assert task.default_if_none("hello", "x") == "hello"

    def check_count_none():
        assert task.count_none([1, None, 2, None, None]) == 3
        assert task.count_none([1, 2, 3]) == 0
        assert task.count_none([]) == 0
        assert task.count_none([None]) == 1

    results.append(run_check("safe_divide", check_safe_divide))
    results.append(run_check("first_or_none", check_first_or_none))
    results.append(run_check("find_index", check_find_index))
    results.append(run_check("default_if_none", check_default_if_none))
    results.append(run_check("count_none", check_count_none))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
