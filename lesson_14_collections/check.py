"""
Проверка задачи урока 14.
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

    def check_process_queue():
        assert task.process_queue(["a", "b", "c"]) == ["a", "b", "c"]
        assert task.process_queue([]) == []
        assert task.process_queue([1]) == [1]

    def check_top_words():
        r = task.top_words(["a", "b", "a", "c", "a", "b"], 2)
        assert r == ["a", "b"], f"получили {r}"
        assert task.top_words(["x"], 1) == ["x"]

    def check_group_by_first_letter():
        r = task.group_by_first_letter(["apple", "ant", "bear"])
        assert isinstance(r, dict), "должен быть dict"
        # сравним содержимое
        assert dict(r) == {"a": ["apple", "ant"], "b": ["bear"]}, f"получили {dict(r)}"

    def check_point():
        assert task.Point is not None, "Point должен быть определён"
        p = task.make_point(1, 2)
        assert p.x == 1 and p.y == 2, f"получили {p}"
        assert tuple(p) == (1, 2)

    def check_count_letters():
        assert task.count_letters("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
        assert task.count_letters("") == {}

    results.append(run_check("process_queue", check_process_queue))
    results.append(run_check("top_words", check_top_words))
    results.append(run_check("group_by_first_letter", check_group_by_first_letter))
    results.append(run_check("Point / make_point", check_point))
    results.append(run_check("count_letters", check_count_letters))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
