"""
Проверка задачи урока 5.
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

    def check_origin():
        assert isinstance(task.origin, tuple), \
            f"origin должен быть tuple, а равен {type(task.origin).__name__}"
        assert task.origin == (0, 0), f"origin должен быть (0, 0), а равен {task.origin}"

    def check_swap():
        assert task.swap(1, 2) == (2, 1)
        assert task.swap("a", "b") == ("b", "a")
        assert isinstance(task.swap(1, 2), tuple), "swap должен возвращать tuple"

    def check_min_max():
        assert task.min_max([3, 1, 4, 1, 5]) == (1, 5)
        assert task.min_max([7]) == (7, 7)
        assert task.min_max([]) == (None, None)

    def check_sum_range():
        assert task.sum_range(1, 5) == 10   # 1+2+3+4
        assert task.sum_range(0, 0) == 0
        assert task.sum_range(0, 10) == 45

    def check_countdown():
        assert task.countdown(5) == [5, 4, 3, 2, 1]
        assert task.countdown(1) == [1]
        assert task.countdown(0) == []

    results.append(run_check("origin", check_origin))
    results.append(run_check("swap", check_swap))
    results.append(run_check("min_max", check_min_max))
    results.append(run_check("sum_range", check_sum_range))
    results.append(run_check("countdown", check_countdown))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
