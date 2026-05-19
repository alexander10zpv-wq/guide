"""
Проверка задачи урока 4.
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

    def check_fruits():
        assert isinstance(task.fruits, list), "fruits должен быть list"
        assert task.fruits == ["apple", "banana", "cherry"], \
            f"fruits должен быть ['apple','banana','cherry'], а равен {task.fruits}"

    def check_add_item():
        assert task.add_item([1, 2], 3) == [1, 2, 3]
        assert task.add_item([], "a") == ["a"]

    def check_remove_item():
        assert task.remove_item([1, 2, 3], 2) == [1, 3]
        # значения нет — список не меняется
        assert task.remove_item([1, 2, 3], 999) == [1, 2, 3]
        assert task.remove_item([], "x") == []

    def check_sum_positive():
        assert task.sum_positive([-1, 2, -3, 4]) == 6
        assert task.sum_positive([1, 2, 3]) == 6
        assert task.sum_positive([-1, -2]) == 0
        assert task.sum_positive([]) == 0

    def check_unique_sorted():
        assert task.unique_sorted([3, 1, 2, 1, 3]) == [1, 2, 3]
        assert task.unique_sorted([]) == []
        assert task.unique_sorted([5]) == [5]

    def check_squares_of_evens():
        assert task.squares_of_evens(6) == [0, 4, 16]
        assert task.squares_of_evens(0) == []
        assert task.squares_of_evens(1) == [0]
        assert task.squares_of_evens(10) == [0, 4, 16, 36, 64]

    results.append(run_check("fruits", check_fruits))
    results.append(run_check("add_item", check_add_item))
    results.append(run_check("remove_item", check_remove_item))
    results.append(run_check("sum_positive", check_sum_positive))
    results.append(run_check("unique_sorted", check_unique_sorted))
    results.append(run_check("squares_of_evens", check_squares_of_evens))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
