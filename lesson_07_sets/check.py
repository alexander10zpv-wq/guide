"""
Проверка задачи урока 7.
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

    def check_unique():
        r = task.unique([1, 2, 2, 3])
        assert isinstance(r, set), f"должно быть set, а {type(r).__name__}"
        assert r == {1, 2, 3}
        assert task.unique([]) == set()

    def check_common():
        r = task.common([1, 2, 3], [2, 3, 4])
        assert isinstance(r, set)
        assert r == {2, 3}
        assert task.common([1, 2], [3, 4]) == set()

    def check_union_all():
        r = task.union_all([[1, 2], [2, 3], [3, 4]])
        assert isinstance(r, set)
        assert r == {1, 2, 3, 4}
        assert task.union_all([]) == set()

    def check_only_in_first():
        r = task.only_in_first([1, 2, 3], [2, 3, 4])
        assert isinstance(r, set)
        assert r == {1}
        assert task.only_in_first([1, 2], [1, 2]) == set()

    def check_has_duplicates():
        assert task.has_duplicates([1, 2, 3]) is False
        assert task.has_duplicates([1, 2, 2]) is True
        assert task.has_duplicates([]) is False

    results.append(run_check("unique", check_unique))
    results.append(run_check("common", check_common))
    results.append(run_check("union_all", check_union_all))
    results.append(run_check("only_in_first", check_only_in_first))
    results.append(run_check("has_duplicates", check_has_duplicates))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
